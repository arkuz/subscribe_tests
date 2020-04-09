import dateutil.parser as isoparser
import pytest
import os
import json


from helpers.api import API
from helpers.readers import read_yaml
import helpers.const as const
import helpers.tools as tools


# коды ответов сервера
STATUS_BAD = 500
STATUS_OK = 200


class TestsSubscribe:
    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))
    api_url = config['api_url']


    def setup_class(self):
        self.api = API(self.api_url)


    def setup_method(self):
        # чистим БД перед каждым тестом
        self.api.delete_subscribers()


    # тест проверяет невозможность добавления подписчика без указния параметров
    @pytest.mark.negative
    def test_add_subscriber_empty_params(self):
        data = {}
        data = json.dumps(data)
        resp = self.api.add_subscriber(data)
        assert resp.status_code == STATUS_BAD
        assert resp.json()['message'] == 'Internal Server Error'


    # тест проверяет невозможность добавления подписчика с некорректным email
    @pytest.mark.negative
    def test_add_subscriber_email_invalid(self):
        email = tools.generate_random_string()
        data = {
            'email': email,
            'name': 'Ivan',
            'time': '7d'
        }
        data = json.dumps(data)
        resp = self.api.add_subscriber(data)
        assert resp.status_code == STATUS_OK
        assert resp.json()['error'] == f"ValidationError (SubscriptionModel:None) (Invalid email address: {email}: ['email'])"


    # тест проверяет добавление подписчика при валидном email и остальных параметрах (пустых или заполненных, в том числе с длиной строки = 1000)
    @pytest.mark.positive
    @pytest.mark.parametrize("email,name,time,comment", [
        (tools.generate_email(), '', '', ''),
        (tools.generate_email(), tools.generate_random_string(), '7d', tools.generate_random_string()),
        (tools.generate_email(), tools.generate_random_string(1000), tools.generate_random_string(1000), tools.generate_random_string(1000)),
    ])
    def test_add_subscriber_with_email_and_any_params(self, email, name, time, comment):
        data = {
            'email': email,
            'name': name,
            'time': time,
            'comment': comment,
        }
        data = json.dumps(data)
        resp = self.api.add_subscriber(data)
        assert resp.status_code == STATUS_OK
        resp = resp.json()
        assert resp['id'] == self.api.get_subscribers().json()[0]['id']


    # тест проверяет удаление подписчиков
    @pytest.mark.positive
    def test_delete_subscribers(self, add_subscriber_fixture):
        count = 5
        add_subscriber_fixture(count)
        resp = self.api.delete_subscribers()
        assert resp.status_code == STATUS_OK
        resp = resp.json()
        assert resp['removed'] == count
        assert not self.api.get_subscribers().json()


    # тест проверяет получение списка подписчиков
    @pytest.mark.positive
    def test_get_subscribers(self, add_subscriber_fixture):
        expected_subs = add_subscriber_fixture(5)
        expected_keys = expected_subs[0]
        resp = self.api.get_subscribers()
        assert resp.status_code == STATUS_OK
        actual_subs = resp.json()
        assert len(actual_subs) == len(expected_subs)
        # проверяем, что ключи и значения добавленных подписчиков есть в актуальном ответе сервера
        for item in actual_subs:
            for k, v in item.items():
                if k in expected_keys:
                    assert tools.is_items_exist_in_list_of_dict(expected_subs, k, v)


    # тест проверяет корректность сроков подписки
    # невалидные параметры устанавливают expired_at == created_at
    @pytest.mark.positive
    @pytest.mark.parametrize("time,delta_sec", [
        ('unknown', 0.0),
        ('6y', 0.0),
        ('23', 0.0),
        ('1D', 0.0),
        ('22H', 0.0),
        ('105M', 0.0),
        ('50S', 0.0),
        ('1d', 86400.0),
        ('22h', 79200.0),
        ('105m', 6300.0),
        ('50s', 50.0),
    ])
    def test_check_subscribe_time(self, time, delta_sec):
        data = {
            'email': tools.generate_email(),
            'name': tools.generate_random_string(),
            'time': time,
        }
        data = json.dumps(data)
        self.api.add_subscriber(data)
        resp = self.api.get_subscribers().json()[0]
        created_at = isoparser.parse(resp['created_at'])
        expired_at = isoparser.parse(resp['expired_at'])
        # вычисляем срок подписки в секундах и допускаем разницу между датами в 0.5 секунды
        delta = expired_at - created_at
        acceptable_delta = abs(delta.total_seconds() - delta_sec)
        assert 0 <= acceptable_delta <= 0.5


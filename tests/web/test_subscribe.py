import pytest
import os
from selenium import webdriver

from helpers.api import API
from helpers.readers import read_yaml
import helpers.const as const
from helpers.browser_setup import config_and_run_browser

from pages.main_page import MainPage


class TestsMain:
    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))
    url = config['site_url']
    api_url = config['api_url']

    driver: webdriver
    driver = None


    def setup_class(self):
        self.api = API(self.api_url)
        self.driver = config_and_run_browser(self.config)

        # для запуска локального браузера
        #self.driver = webdriver.Chrome(executable_path="/Users/arkuz/Repos/subscribe_tests/chromedriver")
        #self.driver.maximize_window()

        self.driver.get(self.url)
        self.main_page = MainPage(self.driver)


    def setup_method(self):
        # чистим БД перед каждым тестом
        self.api.delete_subscribers()
        self.driver.refresh()


    def teardown_class(self):
        self.driver.close()


    # тест проверяет успешную подписку с заполнением всех полей
    @pytest.mark.positive
    def test_add_subscriber_success(self):
        expected_res = {
            'name': 'Ivanov Ivan',
            'email': 'hello@example.com',
            'time': True
        }
        time = '7d'
        self.main_page.subscribe_user(
            email=expected_res['email'],
            name=expected_res['name'],
            time=time,
        )
        actual_res = self.main_page.get_row_data(1)
        assert actual_res == expected_res


    # тест проверяет успешную подписку с заполнением всех полей с невалидной датой подписки
    @pytest.mark.positive
    def test_add_subscriber_invalid_time(self):
        expected_res = {
            'name': 'Ivanov Ivan',
            'email': 'hello@example.com',
            'time': False
        }
        time = 'unknown'
        self.main_page.subscribe_user(
            email=expected_res['email'],
            name=expected_res['name'],
            time=time,
        )
        actual_res = self.main_page.get_row_data(1)
        assert actual_res == expected_res


    # тест проверяет, что подписка НЕ оформилась с незаполненным полем email
    @pytest.mark.negative
    def test_add_subscriber_invalid_email(self):
        data = {
            'name': 'Ivanov Ivan',
            'email': '',
            'time': '7d'
        }
        self.main_page.subscribe_user(
            email=data['email'],
            name=data['name'],
            time=data['time'],
        )
        assert self.main_page.get_rows() is None


    # тест проверяет кнопку рефреша
    @pytest.mark.positive
    def test_refresh_button(self, add_subscriber_fixture):
        row_count = 3
        add_subscriber_fixture(row_count)
        self.main_page.refresh_btn_click()
        assert len(self.main_page.get_rows()) == row_count


    # тест поверяет кнопку удаления
    @pytest.mark.positive
    def test_delete_button(self, add_subscriber_fixture):
        add_subscriber_fixture(7)
        self.main_page.refresh_btn_click()
        self.main_page.delete_btn_click()
        assert self.main_page.get_rows() is None


    # тест проверяет, что таблица отображает 5 последних добавленнх зписей
    @pytest.mark.positive
    def test_last_5_subscribers(self, add_subscriber_fixture):
        api_subscribers_list = add_subscriber_fixture(9)
        self.main_page.refresh_btn_click()
        ui_subscribers_list = self.main_page.get_rows_data()
        assert len(ui_subscribers_list) == 5
        api_subscribers_list.reverse()
        expected_res = []
        actual_res = []
        for i in range(0, len(ui_subscribers_list)):
            expected_res.append({
                'email': api_subscribers_list[i]['email'],
                'name': api_subscribers_list[i]['name'],
            })

            actual_res.append({
                'email': ui_subscribers_list[i]['email'],
                'name': ui_subscribers_list[i]['name'],
            })
        assert actual_res == expected_res


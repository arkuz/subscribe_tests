import json
import os
import pytest

import helpers.const as const
from helpers.api import API
from helpers.readers import read_yaml
from helpers.tools import generate_random_string, generate_email


config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))
api_url = config['api_url']
api = API(api_url)


@pytest.fixture
def add_subscriber_fixture():
    def _method(count=1):
        result_list = []
        for i in range(0, count):
            data = {
                'email': generate_email(),
                'name': generate_random_string(),
                'time': '7d',
            }
            api.add_subscriber(json.dumps(data))
            result_list.append(data)
        return result_list
    return _method


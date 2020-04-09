import os
import json
import random
import string


def get_project_path(path):
    """ Функция возвращает путь до корневой папки проекта """
    proj_name = 'subscribe_tests'
    while os.path.split(path)[1] != proj_name:
        path = os.path.split(path)[0]
    print(path)
    return path


def generate_random_string(length=10):
    """ Функция генерирует случайный набор букв """
    name = ''
    for _ in range(1, length + 1):
        name += random.choice(string.ascii_letters)
    return name


def generate_email():
        return f'{generate_random_string()}@example.com'


def is_items_exist_in_list_of_dict(list, key, value):
    """ Функция принимает на вход список словарей
    и ищет пару key, value перебирая все словари в списке"""
    for el in list:
        for k,v in el.items():
            if k == key and v == value:
                return True
    return False


def print_formatted_json(_json, ensure_ascii=True, indent=2):
    """ Функция печатает отформатированный json. Используется для отладки """
    print(json.dumps(_json, ensure_ascii=ensure_ascii, indent=indent))



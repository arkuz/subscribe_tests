import yaml


def read_yaml(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return yaml.load(data, Loader=yaml.FullLoader)


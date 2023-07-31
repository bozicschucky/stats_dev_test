import json


def read_json_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

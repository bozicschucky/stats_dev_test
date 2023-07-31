import json


def read_json_file(file_path):
    with open(file_path) as f:
        try:
            data = json.load(f)
        except Exception as e:
            print('Invalid file nam', e)
    return data


def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

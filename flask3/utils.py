import json


def get_data(json_file):
    try:
        with open(json_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def update_data(json_file, new_data):
    file_to_update = get_data(json_file)
    file_to_update.append(new_data)
    with open(json_file, 'w') as file:
        json.dump(file_to_update, file)
    return True

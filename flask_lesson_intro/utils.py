import json


def get_data():
    try:
        with open("data.json") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

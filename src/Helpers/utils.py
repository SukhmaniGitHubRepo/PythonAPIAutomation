# Helps to read json files and provide you the json data

import json


def get_pay_load_auth():
    # Read from the auth.json and return json
    file_date = open("src/resources/auth.json")
    data = json.load(file_date)
    file_date.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def token_headers(create_token):
    temp_token = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    return headers

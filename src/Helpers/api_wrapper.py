import requests
import json


def get_request(url, auth, header, in_json, payload):
    get_response_data = requests.get(url=url, headers=header, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return get_response_data.json()
    return get_response_data


def post_request(url, auth, header, in_json, payload):
    post_response_data = requests.post(url=url, auth=auth, headers=header, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def patch_request(url, auth, header, in_json, payload):
    patch_response_data = requests.patch(url=url, auth=auth, headers=header, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_request(url, auth, header, in_json, payload):
    delete_response_data = requests.delete(url=url, auth=auth, headers=header, data=json.dumps(payload))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data

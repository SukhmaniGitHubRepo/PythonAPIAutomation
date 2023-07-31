import os
import json
import pytest
from dotenv import load_dotenv


@pytest.fixture
def load_json_data():
    load_dotenv()
    file_name = os.getenv("load_env")
    print(file_name)
    with open("file_name", 'r') as f:
        # with open('qa_env.json', 'r') as f:
        # data = json.load(f)
        data = json.load(f)
    return data


def test_make_request(load_json_data):
    print(load_json_data["url"])

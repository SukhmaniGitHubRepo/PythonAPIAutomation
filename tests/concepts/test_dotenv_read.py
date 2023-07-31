import os

import pytest
from dotenv import load_dotenv

from src.Constants.apiconstants import url_create_booking, url_update_delete_booking
from src.Helpers.api_wrapper import post_request, patch_request
from src.Helpers.common_verification import verify_http_code, verify_key
from src.Helpers.payload_manager import create_booking, patch_update
from src.Helpers.utils import common_headers

# Declare the global variable booking_id
booking_id = None


@pytest.fixture
def test_create_booking_tc2():
    global booking_id
    response = post_request(url_create_booking(), header=common_headers(), auth=None, in_json=False,
                            payload=create_booking())
    verify_http_code(response, 200)
    booking_id = response.json()["bookingid"]
    print(response.json())
    verify_key(booking_id)
    return booking_id


def test_patch_update_tc3(test_create_booking_tc2):
    global booking_id
    load_dotenv()
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + str(os.getenv("token"))
    }
    temp_token = "token=" + str(os.getenv("token"))
    print(temp_token)
    print(os.getenv("username"))
    response = patch_request(url_update_delete_booking(str(booking_id)),
                             auth=None,
                             header=headers,
                             in_json=False,
                             payload=patch_update())
    verify_http_code(response, 200)
    print(response.json())
    print(booking_id)




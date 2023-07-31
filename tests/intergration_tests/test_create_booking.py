import pytest
import allure
from src.Constants.apiconstants import url_create_booking, url_update_delete_booking, url_create_token
from src.Helpers.api_wrapper import post_request, patch_request, delete_request, get_request
from src.Helpers.common_verification import verify_http_code, verify_key
from src.Helpers.payload_manager import create_booking, patch_update, create_token, get_booking
from src.Helpers.utils import common_headers, token_headers

# Declare the global variable booking_id
booking_id = None


class TestIntegration(object):

    @pytest.fixture
    @pytest.mark.smoke
    @allure.feature("TC#1 - Verify Create Token")
    def test_create_token_tc1(self):
        response = post_request(url_create_token(), header=common_headers(), auth=None, in_json=False,
                                payload=create_token())
        verify_http_code(response, 200)
        token = response.json()["token"]
        print(token)
        return response.json()["token"]

    @pytest.fixture
    @pytest.mark.smoke
    @allure.feature("TC#2 - Verify Create Booking")
    def test_create_booking_tc2(self):
        global booking_id
        response = post_request(url_create_booking(), header=common_headers(), auth=None, in_json=False,
                                payload=create_booking())
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        print(response.json())
        verify_key(booking_id)
        return booking_id

    @pytest.mark.smoke
    @allure.feature("TC#3 - Update the Booking Details")
    def test_patch_update_tc3(self, test_create_token_tc1,test_create_booking_tc2):
        global booking_id
        response = patch_request(url_update_delete_booking(str(booking_id)),
                                 header=token_headers(test_create_token_tc1),
                                 auth=None,
                                 in_json=False,
                                 payload=patch_update())
        verify_http_code(response, 200)
        print(response.json())
        print(booking_id)

    @pytest.mark.smoke
    @allure.feature("TC#4 - Get the Booking Details")
    def test_get_tc4(self):
        global booking_id
        response = get_request(url_update_delete_booking(str(booking_id)),
                               header=common_headers(),
                               auth=None,
                               in_json=False,
                               payload=get_booking())
        verify_http_code(response, 200)
        print(response.json())
        print(booking_id)

    @pytest.mark.smoke
    @allure.feature("TC#5 - Delete the Booking Details")
    def test_delete_tc5(self, test_create_token_tc1):
        global booking_id
        response = delete_request(url_update_delete_booking(str(booking_id)),
                                  header=token_headers(test_create_token_tc1),
                                  auth=None,
                                  in_json=False,
                                  payload=create_booking())
        verify_http_code(response, 201)

    @pytest.mark.smoke
    @allure.feature("TC#6 -Try to Fetch the Deleted Booking Details")
    def test_get_delete_id_tc5(self):
        global booking_id
        response = get_request(url_update_delete_booking(str(booking_id)),
                               header=common_headers(),
                               auth=None,
                               in_json=False,
                               payload=get_booking())
        verify_http_code(response, 404)

# Http Status code
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == int(expected_data), "Expected Status :" + str(expected_data)


def verify_key(key):
    assert key != 0, "key is not empty: " + key
    assert key > 0, "key should be greater than zero: " + key
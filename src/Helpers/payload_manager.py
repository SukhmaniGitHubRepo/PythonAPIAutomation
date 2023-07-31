def create_booking():
    payload = {

        "firstname": "John",
        "lastname": "Cena",
        "totalprice": 7000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": "Breakfast, Lunch"
    }
    return payload


def get_booking():
    payload = {
        "firstname": "Sanjeet",
        "lastname": "Bhavik",
        "totalprice": 112,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2018-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def patch_update():
    payload = {
        "firstname": "Sukhmani",
        "lastname": "K"
    }
    return payload


def create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

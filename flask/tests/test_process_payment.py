"""
Run the unit test suite.
"""
#import pytest
import requests
import json
import datetime

from app import app

from app.models.payment import Payment

def test_endpoint():
    """
    Test that the endpoint is available.
    """
    with app.test_client() as c:
        data = {"card_holder": "John Smith",
            "card_number": "0000-0000-0000-0000",
            "security_code": "333",
            "amount": 10}
        data_j = json.dumps(data)
        response = c.post("http://localhost/payment/create",
                          json=data_j)
    #response = requests.post(url="http://localhost/create/payment", data=data_j,
    #                         headers={"Content-Type": "application/json"})
    assert response.status_code == 200


def test_process_payment_create_db_entry():
    """
    Test that the API call creates the entry in the database.
    """
    with app.test_client() as c:
        data = {"card_holder": "John Smith",
            "card_number": "0000-0000-0000-0000",
            "security_code": "333",
            "amount": 10}
        data_j = json.dumps(data)
        response = c.post("http://localhost/payment/create", json=data_j)



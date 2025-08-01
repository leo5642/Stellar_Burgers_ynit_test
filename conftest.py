import json
import requests
import pytest
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import string 
import random 

@pytest.fixture(scope="class")
def login_gen():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = generate_random_string(10)+ '@test.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    yield payload

@pytest.fixture(scope="class")
def token(login_gen):
    payload = login_gen.copy()
    r = requests.post(UrlCollector.url_register, data=payload)
    payload.pop("name")

    r = requests.post(UrlCollector.url_login, data=payload)
    r = r.json()
    token = r["accessToken"]

    headers = {"Authorization": f"{token}"}
    return headers
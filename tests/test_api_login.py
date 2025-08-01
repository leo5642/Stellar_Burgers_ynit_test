import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestPostCourier2():
    @allure.title('вход под существующим пользователем')
    def test_my_ligin(self):
        payload = AuthData.my_login.copy()

        with allure.step('Отправка авторизации'):
            r = requests.post(UrlCollector.url_login, data=payload)
        assert r.status_code == 200
        payload.pop("password")
        r = r.json()
        assert r["success"] == True
        
    @allure.title('вход с неверным логином и паролем')
    def test_no_valid_email_and_password(self):
        payload = {
        "email": "leo5642@tets.ru123",
        "password": "sdfsdfsdf123"
        }

        with allure.step('Отправка запроса с неверным логином и паролем'):
            r = requests.post(UrlCollector.url_login, data=payload)
        assert r.status_code == 401
        payload.pop("password")
        r = r.json()
        assert r["message"] == "email or password are incorrect"

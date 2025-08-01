import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestPostCourier1():
    @allure.title('создание уникального пользователя')
    def test_add_new_register(self, login_gen):
        payload = login_gen.copy()

        with allure.step('Отправка запроса на регистрацию'):
            r = requests.post(UrlCollector.url_register, data=payload)
        assert r.status_code == 200
        payload.pop("password")
        r = r.json()
        assert r["success"] == True
    
    @allure.title('создание пользователя, который уже зарегистрирован;')
    def test_no_register_dubpl(self, login_gen):
        payload = login_gen.copy()

        requests.post(UrlCollector.url_register, data=payload)
        with allure.step('Повторная отправка запроса на регистрацию с темеже данными'):
            r = requests.post(UrlCollector.url_register, data=payload)
        assert r.status_code == 403
        r = r.json()
        assert r["message"] == 'User already exists'

    @allure.title('создание пользователя и не заполнение одного из обязательных полей. три раза')
    @pytest.mark.parametrize("email", AuthData.my_register)
    def test_no_required_field(self, email):
        payload = AuthData.my_register.copy()
        payload = payload.pop(email)

        with allure.step('Отправка запроса без одного обязательного поля'):
            r = requests.post(UrlCollector.url_register, data=payload)
        assert r.status_code == 403
        r = r.json()
        assert r["message"] == "Email, password and name are required fields"


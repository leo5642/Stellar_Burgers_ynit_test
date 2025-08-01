import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure


class TestPostCourier3():
    @allure.title('Создание заказа с авторизацией')
    def test_order_token(self, token):
        headers = token
        with allure.step('Отправка запроса создания заказа с авторизации'):
            r = requests.post(UrlCollector.url_order, headers=headers)
        
        assert r.status_code == 400
        r = r.json()
        assert r["success"] == False

    @allure.title('Создание заказа без авторизации')
    def test_order_no_token_no_ingridiens(self):
        with allure.step('Отправка запроса создания заказа без авторизации'):
            r = requests.post(UrlCollector.url_order)
        
        assert r.status_code == 400
        r = r.json()
        assert r["success"] == False

    @allure.title('Создание заказа с ингридиентами авторизованого пользователя')
    def test_order_token_ingridiens(self, token):
        headers = token
        payload = AuthData.my_order.copy()
        with allure.step('Отправка запроса создания заказа с ингридиентами авторизованого пользователя'):
            r = requests.post(UrlCollector.url_order, data=payload, headers=headers)
        assert r.status_code == 200
        r = r.json()
        assert r["success"] == True    
    
    @allure.title('создание заказа без ингридиентов и без авторизации')
    def test_order_token_no_ingridiens(self, token):
        headers = token
        payload = []
        with allure.step('Отправка запроса создания заказа без ингридиентов и без авторизации'):
            r = requests.post(UrlCollector.url_order, data=payload, headers=headers)
        assert r.status_code == 400
        r = r.json()
        assert r["success"] == False

    @allure.title('Создание заказа с неверным хешем и автоизованным пользователем')
    def test_order_token_no_valid_id_ingridiens(self, token):
        payload = AuthData.my_order.copy()
        headers = token
        payload = {"ingredients": []}
        with allure.step('Отправка запроса создания заказа с неверным хешем и автоизованным пользователем'):
            r = requests.post(UrlCollector.url_order, data=payload, headers=headers)
        assert r.status_code == 400

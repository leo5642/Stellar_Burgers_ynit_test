from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from pages.page_list_orders import PageOrder
from locators.url import UrlCollector
import allure
from locators.data import AuthData
import string 
import random 
import json
import requests

def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        metafunc.parametrize("browser", ["chrome", "firefox"], indirect=True)

@pytest.fixture(scope="function")
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(UrlCollector.url_home)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/section[2]/div/button"))
    )
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function", autouse=False)
def number_order():
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

    r = requests.post(UrlCollector.url_register, data=payload)
    payload.pop("name")

    r = requests.post(UrlCollector.url_login, data=payload)
    r = r.json()
    token = r["accessToken"]

    headers = {"Authorization": f"{token}"}

    payload = AuthData.my_order.copy()
    with allure.step('Отправка запроса создания заказа с ингридиентами авторизованого пользователя'):
        r = requests.post(UrlCollector.url_order, data=payload, headers=headers)
    r = r.json()
    result = r["order"]["number"]
    return result
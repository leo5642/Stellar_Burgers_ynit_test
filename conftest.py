from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from pages.page_order_scooter import PageOrder
from locators.url import UrlCollector
from locators.data import AuthData
import allure

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Firefox()
    
    driver.get(UrlCollector.url_home)
    yield driver
    
    driver.quit()

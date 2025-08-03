from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector
import allure
from pages.base_page import BasePage

class PageOrder(BasePage):
    
    @allure.step("Метот заполняет поле имя")
    def get_open_url(self, url, locator):
        self.driver.get(url)
        self.find_element(locator)

    @allure.step('Получает текст элемента')
    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text


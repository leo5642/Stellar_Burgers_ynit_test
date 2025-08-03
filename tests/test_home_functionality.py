from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from locators.url import UrlCollector
import allure

class Testbookscollector1:
    @allure.step("Проверка перехода по клику на конструктор")
    def test_use_burron(self, browser):
        home_page = HomePage(browser)

        home_page.click_button_kom()
        current_url = home_page.get_current_url()
        assert current_url == UrlCollector.url_home
    
    @allure.step("Проверка перехода по клику на раздел Лента заказов")
    def test_use_list_order(self, browser):
        home_page = HomePage(browser)

        home_page.click_button_order()
        current_url = home_page.get_current_url()
        assert current_url == UrlCollector.url_list_order

    @allure.step("Проверка перехода на информацию об ингридиенте")
    def test_use_burron1(self, browser):
        home_page = HomePage(browser)

        home_page.click_button_bun()
        text = home_page.get_text_activ()
        
        assert text == 'Детали ингредиента'
    @allure.step("Проверка закрытия формы информации о заказе через крестик")
    def test_use_burron1_click_close(self, browser):
        home_page = HomePage(browser)

        home_page.click_button_bun()
        home_page.click_button_close_bun()
        current_url = home_page.get_current_url()
        assert UrlCollector.url_home in current_url

    @allure.step("Проверка увечелечения счетчика ингридиентов при добавлении ингридиента в заказ")
    def test_numbe_2_in_bun_use_bun(self, browser):
        home_page = HomePage(browser)
        self.driver = browser

        home_page.drag_and_drop_in_konst()
        result = home_page.text_number()
        assert result == '2'
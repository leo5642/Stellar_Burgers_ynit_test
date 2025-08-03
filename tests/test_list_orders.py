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
from pages.page_list_orders import PageOrder
import allure

class Testbookscollector2:
    @allure.step("Проверка увелечения счетчика общего заказов при добавлении заказа")
    def test_sum_order_plus_one(self, browser, request):
        order_bage = PageOrder(browser)
        self.driver = browser
        order_bage.get_open_url(UrlCollector.url_list_order, LocatorsCollector.orders_all_time)
        orders_all = order_bage.get_text(LocatorsCollector.orders_all_time)
       
        order = request.getfixturevalue("number_order")
        assert len(str(order)) == 6
        orders_all1 = order_bage.get_text(LocatorsCollector.orders_all_time)
        
        assert int(orders_all) + 1 == int(orders_all1)

    @allure.step("Проверка увелечения счетчика сегодня заказов при добавлении заказа")
    def test_sum_today_order_plus_one(self, browser, request):
        order_bage = PageOrder(browser)
        self.driver = browser
        order_bage.get_open_url(UrlCollector.url_list_order, LocatorsCollector.orders_today)
        orders_all = order_bage.get_text(LocatorsCollector.orders_today)
       
        order = request.getfixturevalue("number_order")
        assert len(str(order)) == 6
        orders_all1 = order_bage.get_text(LocatorsCollector.orders_today)
        
        assert int(orders_all) + 1 == int(orders_all1)

    @allure.step("Проверка появления номера заказа в списке ленты заказов")
    def test_number_order_in_list_orters(self, browser, request):
        order_bage = PageOrder(browser)
        self.driver = browser
        order_bage.get_open_url(UrlCollector.url_list_order, LocatorsCollector.orders_today)
       
        order = request.getfixturevalue("number_order")
        assert len(str(order)) == 6
        orders_all = order_bage.get_text(LocatorsCollector.number_order_look)
        
        assert '#0' + str(order) == orders_all



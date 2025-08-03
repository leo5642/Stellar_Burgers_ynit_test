from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector
import allure
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    @allure.step("Ожидание появление элемента")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Находит видимый элемент')
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('click по ')
    def click(self, locator):
        element = self.find_visible_element(locator)
        element.click()
    
    @allure.step('Ввод текста')
    def send_keys(self, locator, text):
        element = self.find_visible_element(locator)
        element.send_keys(text)
    
    @allure.step('Получает текст элемента')
    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text
    
    @allure.step("перенос элемента в конструктор")  # как же классно что драг и дроп не учат в процесее обучения и ты должен сам как-то придумать как это делать. Зачем тогда обучение если там нету материала надо сразу диплом давать сдавать
    def drag_and_drop(self, ingredient, target):
        
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()
    
    @allure.step('Переход на старницу')
    def get_use_url(self, url):
        self.driver.get(url)



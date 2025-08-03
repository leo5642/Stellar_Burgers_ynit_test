from selenium.webdriver.common.by import By
import pytest

class LocatorsCollector:
    button_header = (By.XPATH, "//p[contains(@class, 'header__linkText') and text()='Конструктор']")
    button_lenta_order = (By.XPATH, "//p[contains(@class, 'header__linkText') and text()='Лента Заказов']")
    button_ingridient = (By.CLASS_NAME, "counter_counter__ZNLkj")
    text_ingridient = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']")
    button_close_text_ingridient = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS ")
    konstruktor_bun = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS ")
    ingridient_number = (By.CLASS_NAME, 'counter_default__28sqi')
    

    orders_all_time = (By.XPATH, "//*[@id='root']/div/main/div/div/div/div[2]/p[2]")
    orders_today = (By.XPATH, "//*[@id='root']/div/main/div/div/div/div[3]/p[2]")
    number_order_look = (By.CLASS_NAME, "text_type_digits-default")
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # button_text = [
    # (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    # (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    # (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    # (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    # (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    # (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    # (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    # (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    # ]

    # button_close_cooki = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    # button_zakaz_up = (By.CLASS_NAME, "Button_Button__ra12g")
    # button_zakaz_down = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')]")

    # input_name = (By.XPATH, "//input[@placeholder='* Имя']")
    # input_last_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # input_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # input_number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # input_metro = (By.CLASS_NAME, "select-search__input")
    # button_stancia = (By.CLASS_NAME, 'select-search__select')
    # button_next = (By.XPATH, "//button[text()='Далее']")
    # button_logo_scooter = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    # button_logo_yndex = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # input_order_time_now = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # button_order_time_now =(By.CLASS_NAME, "react-datepicker__day")
    # button_time_arend = (By.CLASS_NAME, "Dropdown-placeholder")
    # button_one_day = (By.XPATH, "//div[contains(text(), 'сутки')]")
    # button_collor_black = (By.ID, "black")
    # input_commint = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # button_zakazat = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    # button_yes = (By.XPATH, "//button[text()='Да']")
    # good_complid_order = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    # look_order_status = (By.XPATH, "//button[text()='Посмотреть статус']")
    
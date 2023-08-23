from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
from settings import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Локаторы для тестов
    LOGO = (By.CSS_SELECTOR, "#app-header > div > div > svg") # логотип в шапке слева
    AUTH = (By.XPATH, "//h1[contains(text(), 'Авторизация')]") # начальная страница, заголовок "Авторизация"
    HEADMOBILE = (By.XPATH, "//span[contains(text(), 'Мобильный телефон')]") # поле "Мобильный телефон" по табу "Телефон"
    MAIL = (By.XPATH, "//*[@id='t-btn-tab-mail']") # таб авторизации "Почта"
    HEADMAIL = (By.XPATH, "//span[contains(text(), 'Электронная почта')]") # поле "Электронная почта" по табу "Почта"
    LOGIN = (By.XPATH, "//*[@id='t-btn-tab-login']") # таб авторизации "Логин"
    HEADLOGIN = (By.XPATH, "//span[contains(text(), 'Логин')]") # поле "Логин" по табу "Логин"
    LS = (By.XPATH, "//*[@id='t-btn-tab-ls']") # таб авторизации "Лицевой счёт"
    HEADLS = (By.XPATH, "//span[contains(text(), 'Лицевой счёт')]") # поле "Лицевой счёт" по табу "Лицевой счёт"
    USERNAME = (By.XPATH, '// *[ @ id = "username"]') # поле "Электронная почта" по табу "Почта"
    PASS = (By.XPATH, '//*[@id="password"]') # поле "Пароль" по табу "Почта"
    BUTTON_INPUT = (By.XPATH, '//*[@id="kc-login"]') # кнопка "Войти" по табу "Почта"
    BUTTON_LK = (By.XPATH, '//*[@id="lk-btn"]') # кнопка "Личный кабинет" на странице, открывающейся после успешной авторизации
    ERROR_USERNAME_PASS = (By.XPATH, '// *[ @ id = "form-error-message"]') # сообщение об ошибке "Неверный логин или пароль" по табу "Почта"
    GREY = (By.CSS_SELECTOR, '.rt-link--orange.login-form__forgot-pwd--muted') # ссылка "Забыл пароль" до анимации
    ORANGE = (By.CSS_SELECTOR, '.rt-link--orange.login-form__forgot-pwd--animated') # ссылка "Забыл пароль" после ввода неверного логина и/или пароля
    FORGOT = (By.CSS_SELECTOR, "#forgot_password") # ссылка "Забыл пароль"
    RECOVER = (By.XPATH, "//h1[contains(text(), 'Восстановление пароля')]") # заголовок "Восстановление пароля" на странице по ссылке "Забыл пароль"
    BACK_BUTTON = (By.XPATH, '//*[@id="reset-back"]') # кнопка "Вернуться назад" в форме "Восстановление пароля" на странице по ссылке "Забыл пароль"
    REGISTER_LINK = (By.XPATH, '// *[ @ id = "kc-register"]') # ссылка "Зарегистрироваться" внизу формы авторизации
    REGISTRATION = (By.XPATH, "//h1[contains(text(), 'Регистрация')]") # заголовок "Регистрация" на странице регистрации
    NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input') # поле "Имя" на странице регистрации
    SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input') # поле "Фамилия" на странице регистрации
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input') # поле "Регион" на странице регистрации
    EMAIL = (By.XPATH, '//*[@id="address"]') # поле "E-mail или мобильный телефон" на странице регистрации
    PASSWORD = (By.XPATH, '//*[@id="password"]') # поле "Пароль" на странице регистрации
    PASSWORD_REPEAT = (By.XPATH, '//*[@id="password-confirm"]') # поле "Подтверждение пароля" на странице регистрации
    BUTTON_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button') # кнопка "Зарегистрироваться" на странице регистрации
    VERIFICATION_EMAIL = (By.XPATH, "//h1[contains(text(), 'Подтверждение email')]") # заголовок "Подтверждение email" на странице, открывающейся кнопкой "Зарегистрироваться"
    ERROR_HINT_EMAIL = (By.XPATH, "//span[contains(text(), 'Введите телефон в формате')]") # подсказка при неверно заполненном поле "E-mail или мобильный телефон" на странице регистрации
    ERROR_HINT_NAME = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле')]") # подсказка при неверно заполненном поле "Имя" на странице регистрации

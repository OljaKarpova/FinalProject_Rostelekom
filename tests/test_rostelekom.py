from pages.Main_page import MainPage
from settings import valid_pass, valid_email, invalid_pass, invalid_email, name, surname, region, email, \
    password, false_email, false_mobile10, false_mobile13, false_name1, false_name31, \
    false_name_latin, false_name2, false_name30


# Для запуска кода необходимо ввести следующую команду в терминале:
# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_rostelekom.py
# Для запуска кода на ОС Windows следует ставить обратный слеш:
# python -m pytest -v --driver Chrome --driver-path \tests\chromedriver.exe tests\test_rostelekom.py

# Тест-кейс RTK-001 - Загрузка главной страницы сайта в неавторизованном режиме
def test_1_correct_page(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.LOGO)
    auth = main_page.is_visible(MainPage.AUTH)
    assert logo == True and auth == True

# Тест-кейс RTK-002 - При загрузке страницы по умолчанию выбрана форма авторизации по телефону
def test_2_mobile_auth_by_default(driver):
    main_page = MainPage(driver)
    headmobile = main_page.is_visible(MainPage.HEADMOBILE)
    assert headmobile == True

# Тест-кейс RTK-003 - Таб "Почта" открывает форму авторизации с полем "Электронная почта"
def test_3_email_tab(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL)
    headmail = main_page.is_visible(MainPage.HEADMAIL)
    assert headmail == True

# Тест-кейс RTK-004- Таб "Логин" открывает форму авторизации с полем "Логин"
def test_4_login_tab(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.LOGIN)
    headlogin = main_page.is_visible(MainPage.HEADLOGIN)
    assert headlogin == True

# Тест-кейс RTK-005- Таб "Лицевой счёт" открывает форму авторизации с полем "Лицевой счёт"
def test_5_ls_tab(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.LS)
    headlogin = main_page.is_visible(MainPage.HEADLS)
    assert headlogin == True

# Тест-кейс RTK-006 - Авторизация по валидным email и паролю
def test_6_auth_via_valid_data(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    lk = main_page.is_visible(MainPage.BUTTON_LK)
    assert lk == True

# Тест-кейс RTK-007 - Авторизация по валидному email и НЕвалидному паролю
def test_7_auth_via_invalid_pass(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_pass = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error_pass == True

# Тест-кейс RTK-008 - Авторизация по НЕвалидному email и валидному паролю
def test_8_auth_via_invalid_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_username = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error_username == True

# Тест-кейс RTK-009 - При авторизации по НЕвалидному паролю ссылка "Забыл пароль" становится оранжевой
def test_9_orange_color_invalid_pass(driver):
    main_page = MainPage(driver)
    grey = main_page.is_visible(MainPage.GREY)
    assert grey == True
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    orange = main_page.is_visible(MainPage.ORANGE)
    assert orange == True

# Тест-кейс RTK-010 - Ссылка "Забыл пароль" открывает форму "Восстановление пароля"
def test_10_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    recovery = main_page.is_visible(MainPage.RECOVER)
    assert recovery == True

# Тест-кейс RTK-011 - Кнопка "Вернуться назад" в форме "Восстановление пароля" открывает форму "Авторизация"
def test_11_back_button(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    main_page.find_click(MainPage.BACK_BUTTON)
    auth = main_page.is_visible(MainPage.AUTH)
    assert auth == True

# Тест-кейс RTK-012 - Ссылка "Зарегистрироваться" открывает форму "Регистрация"
def test_12_registration_button(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    reg = main_page.is_visible(MainPage.REGISTRATION)
    assert reg == True

# Тест-кейс RTK-013 - Заполнение формы "Регистрация" корректными данными ведёт на страницу подтверждения email
def test_13_registration_correct_data(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.is_visible(MainPage.VERIFICATION_EMAIL)
    assert valid_reg == True

# Тест-кейс RTK-014 - Заполнение формы "Регистрация" некорректным именем (1 кириллический символ) выдает подсказку
def test_14_registration_incorrect_name_1letter(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, false_name1)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.is_visible(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == True

# Тест-кейс RTK-015 - Заполнение формы "Регистрация" корректным именем (2 кириллических символа) ведёт на страницу подтверждения email
def test_15_registration_correct_name_2letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, false_name2)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.is_visible(MainPage.VERIFICATION_EMAIL)
    assert valid_reg == True

# Тест-кейс RTK-016 - Заполнение формы "Регистрация" корректным именем (30 кириллических символов) ведёт на страницу подтверждения email
def test_16_registration_correct_name_30letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, false_name30)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.is_visible(MainPage.VERIFICATION_EMAIL)
    assert valid_reg == True

# Тест-кейс RTK-017 - Заполнение формы "Регистрация" некорректным именем (31 кириллический символ) выдает подсказку
def test_17_registration_incorrect_name_31letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, false_name31)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.is_visible(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == True

# Тест-кейс RTK-018 - Заполнение формы "Регистрация" некорректным именем (латинские символы) выдает подсказку
def test_18_registration_incorrect_name_latin(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, false_name_latin)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.is_visible(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == True

# Тест-кейс RTK-019 - Заполнение формы "Регистрация" некорректным email выдает подсказку
def test_19_registration_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.is_visible(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == True

# Тест-кейс RTK-020 - Заполнение формы "Регистрация" некорректным номером телефона (13 цифр) выдает подсказку
def test_20_registration_incorrect_mobile_13digits(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile13)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.is_visible(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == True

# Тест-кейс RTK-021 - Заполнение формы "Регистрация" некорректным номером телефона (10 цифр) выдает подсказку
def test_21_registration_incorrect_mobile_10digits(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER_LINK)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile10)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.is_visible(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == True
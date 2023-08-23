import os

from dotenv import load_dotenv

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

# Данные для валидной авторизации
load_dotenv()
valid_email = os.getenv('valid_email')
valid_pass = os.getenv('valid_pass')

# Данные для невалидной авторизации
invalid_email = 'olga@mail.ru'
invalid_pass = '0122222Yy'

# Данные для корректной регистрации
name = 'Олег'
surname = 'Иванов'
region = 'Москва г'
email = 'katyavasyasonya@mail.ru'
password = '111222333Pp'

# Данные для некорректной регистрации и проверки граничных значений
false_name1 = 'Б'
false_name2 = 'Ян'
false_name30 = 'ёйцукенгшщзхъфывапролджэячсмит'
false_name31 = 'ёйцукенгшщзхъфывапролджэячсмить'
false_name_latin = 'Harry'
false_email = 'oleg@mail'
false_mobile13 = '+3751234567891'
false_mobile10 = '+8123456789'
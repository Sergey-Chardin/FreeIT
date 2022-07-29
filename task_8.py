# task_8.py
# Zoom/Сергей; github.com/Sergey-Chardin; Telegram/Nygell Hardbard

# 8.1 Зарегистрировался на сайте: https://openexchangerates.org
# Получил App ID: f79098f7a53943e697db8b6221962000,(выбрал бесплатный план)
# 8.2 Изучил документацию сервиса: https://docs.openexchangerates.org/
# Пишем программу для сбора данных о курсах валют:
import requests
import logging


# 8.5 Логируем
logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
try:
    logging.info('Идет процесс сбора данных')
except Exception:
    logging.debug('Это сообщение об отладке')
# 8.3 Собираем данные о курсах валют за последних 30 календарных дней
# Для примера показаны данные за 25.07.2022
historical25 = requests.get('https://openexchangerates.org/api/historical/2022-07-25.json?app_id=f79098f7a53943e697db8b6221962000')
print(historical25.text)
# 8.4 Создаем справочник кодов валют и их названий	
currencies = requests.get('https://openexchangerates.org/api/currencies.json')
print(currencies.text)
# 8.4 Записываем собранные данные в файлы txt, преобразовывая их в строки
historical_of_currency = historical25.json()
historical_of_currency_str = str(historical_of_currency)
print(historical_of_currency_str)
name_of_currency = currencies.json()
name_of_currency_str = str(name_of_currency)
print(name_of_currency_str)
with open('historical.txt', 'w') as file:
    file.write(historical_of_currency_str)
# ВНИМАНИЕ! Здесь выдает различные ошибки связанные с кодированием. Как решить пока не знаю
with open('currencies.txt', 'w') as file:
    file.write(name_of_currency_str.encode('utf8'))
# 8.7 Зарегистрировался на сайте: https://www.postman.com


# task_5.py
# Zoom/Сергей; github.com/Sergey-Chardin; Telegram/Nygell Hardbard
# Работа с функциями
# 6.1 Я сдаюсь. Я разобрался как создавать файлы, записывать в них текст и т.п.
# но я не нашел способа как с помощью функции вводить текст, который бы
# записывался в файл. Завис на этом:
def savestr(file_text):
    with open('./test_text.txt', 'a') as file:
        file.write(new_str)

print('Введите строку для записи в файл:')
new_str = input()
with open('./test_text.txt') as file:    
    data = file.read()
print(data)
# 6.2
def season(month):
    if 0 < month < 3 or month == 12: 
        return 'зима'
    elif 2 < month < 6: 
        return 'весна'
    elif 5 < month < 9: 
        return 'лето'
    elif 8 < month < 12: 
        return 'осень'

print('Ведите номер месяца:')
month = int(input())
if 12 <month or month< 1:
    print('В григорианском календаре только 12 месяцев.')
    print('''А вот на Марсе можно использовать дарианский
календарь с 24 месяцами''')
else:
    print('Время года:')
    print(season(month))
# 6.3
def square(n):
    return n*4, n**2, round((n**2 * 2)**0.5)

print('Введите сторону квадрата:')
n = int(input())
if n < 1:
    print('Сторона квадрата может быть отрицательной только в неевклидовой геометрии')
else:
    print('Диагональ квадрата/периметр квадрата/площадь квадрата:')
    print(square(n))
# 6.4
def deposit(a, years):
    return  a + (a*0.1)

print('Введите размер вклада в гривнах:')
a = float(input())
print('Введите срок вклада в годах):')
years = int(input())
for i in range(years):
    a = deposit(a, years)
print('Сумма вклада к выдаче:')
print(deposit(a, years))
# 6.5
import time


# Функция-декоратор
def inner_decorator(decorate_function):
    def outer_decorator():
        time_before = time.perf_counter()
# Декорируемая функция
        decorate_function(round(((55760000/speed)/24)/365))
        time_after = time.perf_counter()
        print()
        print(f'Время до вычисления: {time_before}')
        print(f'Время после вычисления: {time_after}')
        print(f'Вычисление заняло: {time_after - time_before:0.4} секунд')
# Выход из функции-декоратора
    return outer_decorator

print('Введите скорость (км/ч), с которой вы обычно перемещаетесь по городу:')
speed = int(input())
def measuring_time(decorate_function):
    print(f'С этой скоростью вы доберетесь до Марса за {decorate_function} лет')
full_function = inner_decorator(measuring_time)
full_function()

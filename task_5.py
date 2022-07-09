# task_5.py
# Zoom/Сергей; github.com/Sergey-Chardin; Telegram/Nygell Hardbard
# Простой калькулятор
error_1 = 'Неверный ввод. Это горячие клавиши. Повторите ввод'
error_2 = 'Неверный ввод. Это не целое число. Повторите ввод'
condition_0 = 'Введите число a и b:'
result_0 = 'Результат вычисления:'
action = 1
while action == 1:
# Выбор действий
    print()
    print('Выберите действие:')
    print('c – калькулятор c целыми числами')
    print('q – выйти из калькулятора')
    print()
    q = 1
    while q == 1:
        try:
            calculator_action = input()
            q = 0
        except KeyboardInterrupt:
            print(f'{error_1}') 
    if calculator_action == 'c':
        clc_action = 1
        while clc_action == 1:
            print()
            print('Введите символ операции:')
            print('+ – сложение')
            print('- – вычитание')
            print('* – умножение')
            print('/ – деление')           
            print('0 – выход из меню')
            q = 1
            while q == 1:
                try:
                    addition = input()
                    q = 0
                except KeyboardInterrupt:
                    print(f'{error_1}') 
            if addition == '0':
                clc_action = 0
# Сложение
            if addition == '+':
                print()
                print(f'{condition_0}')
                q = 1
                while q == 1:
                    try:
                        a, b = int(input()),int(input())
                        q = 0
                        c = a + b
                        print(f'{ result_0}')
                        print(a, '+', b, '=', c)
                    except ValueError:
                        print(f'{error_2}')
                    except KeyboardInterrupt:
                        print(f'{error_1}') 
                else:
                    print()
# Вычитание
            if addition == '-':
                print()
                print('Введите число a и b:')
                q = 1
                while q == 1:
                    try:
                        a, b = int(input()),int(input())
                        q = 0
                        c = a - b
                        print(f'{ result_0}')
                        print(a, '-', b, '=', c)
                    except ValueError:
                        print(f'{error_2}')
                    except KeyboardInterrupt:
                        print(f'{error_1}') 
                else:
                    print()
# Умножение
            if addition == '*':
                print()
                print(f'{condition_0}')
                q = 1
                while q == 1:
                    try:
                        a, b = int(input()),int(input())
                        q = 0
                        c = a * b
                        print(f'{ result_0}')
                        print(a, '*', b, '=', c)
                    except ValueError:
                        print(f'{error_2}')
                    except KeyboardInterrupt:
                        print(f'{error_1}') 
                else:
                    print()
# Деление
            if addition == '/':
                print()
                print(f'{condition_0}')
                q = 1
                while q == 1:
                    try:
                        a, b = int(input()),int(input())
                        if a != 0 and b == 0:
                            print('Это не вещественная арифметика, делить на ноль нельзя.')
                            print('''21 сентября 1997 года в результате деления на ноль в
компьютеризированной управляющей системе крейсера 
USS Yorktown (CG-48) Военно-морского флота США 
произошло отключение всего электронного оборудования 
в системе, в результате чего силовая установка 
корабля прекратила свою работу''')
                            print(f'{condition_0}')
                        elif a == 0 and b == 0:
                            print(f'{ result_0}')
                            print(a, '/', b, '= неопределенность')
                        else:
                            q = 0
                            c = round((a / b), 1)
                            print(a, '/', b, '=', c)
                    except ValueError:
                        print(f'{error_2}')
                    except KeyboardInterrupt:
                        print(f'{error_1}')
                else:
                    print()
# Выход из калькулятора
    if calculator_action == 'q':
        action = 0
        print('Конец вычислений')
        break
    if calculator_action != '+' and calculator_action != '-' and calculator_action != '*' and calculator_action != '/' and calculator_action != 'q':
        print()
        print('Неверный ввод')

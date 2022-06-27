"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import datetime


def comma_to_dot (str):
    if str.count(',') > 0:
        if str.find(',') > 0:
            str = str[:str.find(',')] + '.' + str[str.find(',') + 1:]
        else:
            str = '.' + str[1:]
    return(str)


def str_is_float_number (str):
    if len(str) > 0:
        if str.count(',') + str.count('.') > 1:
            result = False
        else:
            i = 0
            while i < len(str):
                if str[i] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ','):
                    result = False
                    i = len(str)
                else:
                    result = True
                i += 1
    else:
        result = False

    return(result)

balance = 0.0
history = {}
purchase_number = 0
while True:
    print('-' * 10)
    print ('Текущий счет:', balance)
    print('-' * 10)
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print('-' * 10)


    choice = input('Выберите пункт меню: ')
    if choice == '1':
        summ_enter = False
        while summ_enter == False:
            summ = input('На какую сумму пополнить счет: ')
            summ_enter = str_is_float_number(summ)
            if summ_enter == False:
                print('Введено не корректное число!')

        summ = float(comma_to_dot(summ))
        balance += summ

    elif choice == '2':
        price_enter = False
        while price_enter == False:
            price = input('Цена покупки: ')
            price_enter = str_is_float_number(price)
            if price_enter == False:
                print('Введено не корректное число!')

        price = float(comma_to_dot(price))
        if balance >= price:
            purchase = input('Введите название покупки: ')
            history[purchase_number] = [purchase, price]
            balance -= price
            purchase_number += 1
        else:
            print('На счете недостаточно денег.')

    elif choice == '3':
        history_keys = tuple(history.keys())
        for index in range(len(history_keys)):
            print('Покупка:', list(history[history_keys[index]])[0], 'Цена:', list(history[history_keys[index]])[1])

        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

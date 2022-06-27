import os
import platform
import shutil

from pathlib import Path

def print_menu():
    print('  1. Cоздать папку', '\n',
          ' 2. Удалить (файл/папку)', '\n',
          ' 3. Копировать (файл/папку)', '\n',
          ' 4. Просмотр содержимого рабочей директории', '\n',
          ' 5. Посмотреть только папки', '\n',
          ' 6. Посмотреть только файлы', '\n',
          ' 7. Просмотр информации об операционной системе', '\n',
          ' 8. Создатель программы', '\n',' 9. Играть в викторину', '\n',
          '10. Мой банковский счет', '\n',
          '11. Смена рабочей директории (*необязательный пункт)', '\n',
          '12. Выход')


def menu_choose():
    menu = ''
    while not menu.isnumeric():
        menu = input('Выберите пункт меню(1-12): ').strip()
        if menu.isnumeric():
            if int(menu) < 1 or int(menu) > 12:
                print('Введено некорректное значение.')
                menu = ''
        else:
            print('Введено некорректное значение.')
    return menu


home_dir = os.getcwd() # на случай если в п.11 изменят директорию, для запуска игр
while 1 > 0:
    print_menu()
    menu = int(menu_choose())

    if menu == 1: # Cоздать папку
        folder = input('Введите имя создаваемой папки: ')
        if not os.path.isdir(folder):
            os.mkdir(folder)
        else:
            print('Папка ' + folder + ' уже существует.')

    elif menu == 2: # Удалить (файл/папку)
        folder = input('Введите имя удаляемого файла/папки: ')

        if os.path.exists(folder):
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            else:
                os.remove(folder)
        else:
            print('Папка/файл ' + folder + ' не существует.')

    elif menu == 3: # Копировать (файл/папку)
        folder = input('Введите имя копируемого файла/папки: ')
        if os.path.exists(folder):
            if os.path.isdir(folder):
                copy_from = os.path.join(os.getcwd(), folder)
                copy_to = os.path.join(os.getcwd(), 'Copy', folder)
                if not os.path.exists(copy_to):
                    shutil.copytree(folder, copy_to)
                else:
                    print('Копирование невозможно, т.к. в папке назначения уже есть копируемая папка.')
            else:
                if not os.path.exists(copy_to):
                    os.mkdir(copy_to)
                copy_from = os.path.join(os.getcwd(), folder)
                copy_to = os.path.join(os.getcwd(), 'Copy')
                shutil.copy(copy_from, copy_to)
        else:
            print('Папка/файл ' + folder + ' не существует.')

    elif menu == 4: # Просмотр содержимого рабочей директории
        files = os.listdir()
        for index in range(len(files)):
            print(files[index])

    elif menu == 5: # Посмотреть только папки
        # print("Все папки:", os.listdir(folder))
        files = os.listdir()
        for index in range(len(files)):
            if os.path.isdir(files[index]):
                print(files[index])

    elif menu == 6: # Посмотреть только файлы
        print("Все файлы:", os.listdir())
        files = os.listdir()
        for index in range(len(files)):
            if os.path.isfile(files[index]):
                print(files[index])

    elif menu == 7: # Просмотр информации об операционной системе
        uname = platform.uname()
        print('Система: ', uname.system)
        print('Выпуск: ', uname.release)
        print('Версия: ', uname.version)
        print('Процессор: ', uname.processor)
        print('Имя ПК: ', uname.node)

    elif menu == 8: # Создатель программы
        uname = platform.uname()
        print('Система: ', uname.system)
        if uname.system == 'Linux':
            print(Path('manager.py').owner())
        else:
            print('Не нашёл, как на Windows реализовать этот пункт.')
            print('Вариант для Linux:  Path(''manager.py'').owner()')

    elif menu == 9: # Играть в викторину
        os.startfile(os.path.join(home_dir, 'victory.py')) # на случай если в п.11 изменят директорию, для запуска игр

    elif menu == 10: # Мой банковский счет
        os.startfile(os.path.join(home_dir, 'use_functions.py')) # на случай если в п.11 изменят директорию, для запуска игр

    elif menu == 11: # Смена рабочей директории (*необязательный пункт)
        new_path = input('Сменить рабочую директорию на: ')
        try:
            os.chdir(new_path)
            print("Текущая рабочая директория:", os.getcwd())
        except FileNotFoundError:
            print('Указан не верный путь.')

    elif menu == 12: # Выход
        break

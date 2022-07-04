import os
import platform
import shutil
from pathlib import Path


def separato_20_stars(func):
    def inner(*args, **kwargs):
        print('*'*20)
        result = func(*args, **kwargs)
        return result
    return inner


@separato_20_stars
def print_menu():
    print('  1. Cоздать папку', '\n',
          ' 2. Удалить (файл/папку)', '\n',
          ' 3. Копировать (файл/папку)', '\n',
          ' 4. Просмотр содержимого рабочей директории', '\n',
          ' 5. Cохранить содержимое рабочей директории в файл', '\n',
          ' 6. Посмотреть только папки', '\n',
          ' 7. Посмотреть только файлы', '\n',
          ' 8. Просмотр информации об операционной системе', '\n',
          ' 9. Создатель программы', '\n',
          '10. Играть в викторину', '\n',
          '11. Мой банковский счет', '\n',
          '12. Смена рабочей директории (*необязательный пункт)', '\n',
          '13. Выход')


@separato_20_stars
def menu_choose():
    menu = ''
    while not menu.isnumeric():
        menu = input('Выберите пункт меню(1-13): ').strip()
        if menu.isnumeric():
            if int(menu) < 1 or int(menu) > 13:
                print('Введено некорректное значение.')
                menu = ''
        else:
            print('Введено некорректное значение.')
    return menu


def copy_file_folder(folder, destination_folder):
    if os.path.exists(folder):
        if os.path.isdir(folder):
            copy_to = os.path.join(os.getcwd(), destination_folder, folder)
            shutil.copytree(folder, copy_to) if not os.path.exists(copy_to) else print('Копирование невозможно, т.к. в папке назначения уже есть копируемая папка.')
        else:
            copy_from = os.path.join(os.getcwd(), folder)
            copy_to = os.path.join(os.getcwd(), destination_folder)
            if not os.path.exists(copy_to):
                os.mkdir(copy_to)
            shutil.copy(copy_from, copy_to)
    else:
        print('Папка/файл ' + folder + ' не существует.')


def change_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        return False
    else:
        return True


def file_or_folder_from_dir(path, folder): # folder: True = папки, False = файлы
    filter_files = []
    files = os.listdir(path)
    for index in range(len(files)):
        if folder == True:
            if os.path.isdir(files[index]):
                filter_files.append(files[index])
        else:
            if os.path.isfile(files[index]):
                filter_files.append(files[index])
    return filter_files


@separato_20_stars
def print_list_in_line(work_list, separator):
    len_work_list = len(work_list)
    [print(work_list[index], end='.\n' if index == len_work_list - 1 else separator) for index in range(len_work_list)]


def list_to_file(file, work_list):
    [file.write(work_list[index]) if index == 0 else file.write(', ' + work_list[index]) for index in range(len(work_list))]


if __name__ == '__main__':
    home_dir = os.getcwd() # на случай если в п.12 изменят директорию, для запуска игр
    while 1 > 0:
        print_menu()
        menu = int(menu_choose())

        if menu == 1: # Cоздать папку
            folder = input('Введите имя создаваемой папки: ')
            os.mkdir(folder) if not os.path.isdir(folder) else print('Папка ' + folder + ' уже существует.')

        elif menu == 2: # Удалить (файл/папку)
            folder = input('Введите имя удаляемого файла/папки: ')
            shutil.rmtree(folder) if os.path.isdir(folder) else os.remove(folder) if os.path.exists(folder) else print('Папка/файл ' + folder + ' не существует.')

        elif menu == 3: # Копировать (файл/папку)
            folder = input('Введите имя копируемого файла/папки: ')
            copy_file_folder(folder, 'Copy')

        elif menu == 4: # Просмотр содержимого рабочей директории
            files = os.listdir()
            [print(file) for file in files]

        elif menu == 5: # Cохранить содержимое рабочей директории в файл
            with open('listdir.txt', 'w', encoding='utf-8') as list_dir:
                folder_name = file_or_folder_from_dir(os.getcwd(), True)
                file_name = file_or_folder_from_dir(os.getcwd(), False)
                list_dir.write('Папки: ')
                list_to_file(list_dir, folder_name)
                list_dir.write('\nФайлы: ')
                list_to_file(list_dir, file_name)

        elif menu == 6: # Посмотреть только папки
            folder_name = file_or_folder_from_dir(os.getcwd(), True)
            print('Папки:')
            print_list_in_line(folder_name, '; ')

        elif menu == 7: # Посмотреть только файлы
            file_name = file_or_folder_from_dir(os.getcwd(), False)
            print('Файлы:')
            print_list_in_line(file_name, '; ')

        elif menu == 8: # Просмотр информации об операционной системе
            uname = platform.uname()
            print('Система: ', uname.system)
            print('Выпуск: ', uname.release)
            print('Версия: ', uname.version)
            print('Процессор: ', uname.processor)
            print('Имя ПК: ', uname.node)

        elif menu == 9: # Создатель программы
            uname = platform.uname()
            print('Система: ', uname.system)
            if uname.system == 'Linux':
                print(Path('manager.py').owner())
            else:
                print('Не нашёл, как на Windows реализовать этот пункт.')
                print('Вариант для Linux:  Path(''manager.py'').owner()')

        elif menu == 10: # Играть в викторину
            os.startfile(os.path.join(home_dir, 'victory.py')) # на случай если в п.11 изменят директорию, для запуска игр

        elif menu == 11: # Мой банковский счет
            os.startfile(os.path.join(home_dir, 'use_functions.py')) # на случай если в п.11 изменят директорию, для запуска игр

        elif menu == 12: # Смена рабочей директории (*необязательный пункт)
            new_path = input('Сменить рабочую директорию на: ')
            print("Текущая рабочая директория:", os.getcwd()) if change_dir(new_path) else print('Указан не верный путь.')

        elif menu == 13: # Выход
            break

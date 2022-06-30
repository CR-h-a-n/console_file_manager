from use_functions import comma_to_dot, str_is_float_number
from manager import copy_file_folder
import os
import shutil


def test_comma_to_dot():
    test_string_first_comma = ',abc'
    test_string_last_comma = 'abc,'
    test_string_mid_comma = 'a,bc'
    test_string_letters = 'abc'

    assert comma_to_dot(test_string_first_comma) == '.abc'
    assert comma_to_dot(test_string_last_comma) == 'abc.'
    assert comma_to_dot(test_string_mid_comma) == 'a.bc'
    assert comma_to_dot(test_string_letters) == 'abc'


def test_str_is_float_number():
    assert str_is_float_number(',021') == True
    assert str_is_float_number('021,') == True
    assert str_is_float_number('0,21') == True
    assert str_is_float_number('.021') == True
    assert str_is_float_number('021.') == True
    assert str_is_float_number('0.21') == True
    assert str_is_float_number('021,') == True
    assert str_is_float_number('021') == True
    assert str_is_float_number('021,') == True
    assert str_is_float_number('0,21') == True
    assert str_is_float_number('021,') == True

    assert str_is_float_number(' 0,21') == False
    assert str_is_float_number('0,21 ') == False
    assert str_is_float_number('021v') == False
    assert str_is_float_number('0,2b1') == False


def test_copy_file_folder():

    folder_name = 'test_folder'
    file_name = 'test_file.txt'
    copy_folder_name = 'copy_test_folder'

    # проверяем свободны ли имена файла и папки для использования в тесте
    # если нет, то выбираем другие имена
    # если да, создаем файл и папку для теста


    while os.path.exists(folder_name):
        folder_name += '7_3_5'      # меняем имя, добавляя к текущему имени 7_3_5
    os.mkdir(folder_name)

    while os.path.exists(file_name):
        file_name = file_name[:-4] + '7_3_5' + '.txt'      # меняем имя, добавляя к текущему имени 7_3_5
    my_file = open(file_name, "w+")
    my_file.close()

    while os.path.exists(copy_folder_name):
        copy_folder_name += '7_3_5'      # меняем имя, добавляя к текущему имени 7_3_5
    os.mkdir(copy_folder_name)

    # запускаем функцию с подобранными и только что созданными папками и файлами
    copy_file_folder(folder_name, copy_folder_name)     # копируем папку
    copy_file_folder(file_name, copy_folder_name)       # копируем файл

    # проверяем наличие копируемых папки и файла в папке для тестового копирования copy_folder_name
    assert os.path.exists(os.path.join(os.getcwd(), copy_folder_name, folder_name))
    assert os.path.exists(os.path.join(os.getcwd(), copy_folder_name, file_name))

    # удаляем все созданные для теста папки и файлы
    shutil.rmtree(folder_name)
    os.remove(file_name)
    shutil.rmtree(copy_folder_name)


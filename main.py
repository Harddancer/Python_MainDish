# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:35:04 2021

@author: mvandron
"""
import sys

from core import get_list,create_file,create_folder,delete,copy,save_info,ch_folder,games

save_info('Начало')

try:
    command = sys.argv[1]
except IndexError:
    print('Нет аргументов')

try:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Имя файла?')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Имя папки?')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Ни папки ни файла')
        else:
            delete(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Нет исходника')
        try:
            name_1 = sys.argv[3]
        except IndexError:
            print('Какая новая папка')
        else:
            copy(name, name_1)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - изменение рабочей папки')
        print('game - игра "угадай число"')
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Путь к папке')
        else:
            ch_folder(name)
    elif command == 'games':
        games()
except NameError:
    print('Введите команду')

save_info('Конец')




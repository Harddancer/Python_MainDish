#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:34:02 2021

@author: yamamotod
"""


import Class_Employer
import pickle

LOOK = 1
ADD =2
CH =3
DEL = 4
QUIT = 5

def employer():    
    names = ['Сьюзан Майерс','Maрк Джоунс','Джой РОджерс']
    ident = [324,234,765]
    cab = ['Бухгалтерия','Производство','Логистика']
    post = ['Диреткор','Программист','Инженер']
    dictin = {}
    with open('empl.dat','wb') as file_empl:
        for x,y,z,a in zip(names,ident,cab,post):
            my_obj = Class_Employer.Employer(x,y,z,a)
            dictin[y] = my_obj
            print(dictin)
            pickle.dump(dictin,file_empl)
            print('Файл записан')



    
def load_employers():
    
        
    try:
        file_on = open('empl.dat','rb')
        employer_dict = pickle.load(file_on)
        return employer_dict
        print(employer_dict)
        file_on.close()
    except IOError:
        employer_dict = {}
    return employer_dict
    names = ['Сьюзан Майерс','Maрк Джоунс','Джой РОджерс']
    ident = [324,234,765]
    cab = ['Бухгалтерия','Производство','Логистика']
    post = ['Диреткор','Программист','Инженер']
    dictin = {}
    with open('empl.dat','wb') as file_empl:
        for x,y,z,a in zip(names,ident,cab,post):
            my_obj = Class_Employer.Employer(x,y,z,a)
            dictin[y] = my_obj
            print(dictin)
            pickle.dump(dictin,file_empl)
            print('Файл записан')



    
def load_employers2():
    
        
    try:
        file_on = open('empl.dat','rb')
        employer_dict = pickle.load(file_on)
        return employer_dict
        print(employer_dict)
        file_on.close()
    except IOError:
        employer_dict = {}
    return employer_dict

def get_menu_employer():
    print()
    print('Меню')
    print('-----------------------------')
    print('Найти')
    print('Добавить')
    print('Изменить')
    print('Удалить')
    print('Выйти')
    print()
    choice = int(input('Выберите пункт'))
    while choice < LOOK or choice > QUIT:
        choice = int(input('Выберите пункт'))
    return choice
def look(employer_dict):
    id_id = int(input('Введите номер ID'))
    print(employer_dict.get(id_id,'Этот ID  не найден'))
    
def add(employer_dict):
    names = input('Введите имя')
    ident = int(input('Введите номер'))
    cab = input('Введите кабинет')
    post = input('Введите должность')
    my_employer = Class_Employer.Employer(names,ident,cab,post)
    print(my_employer)
    if ident not in employer_dict:
        employer_dict[ident] = my_employer
        print('запись добавлена')
    else:
        print('запись есть')
        
def change(employer_dict):
    ident = input ( 'Введите номер: ' )
    if ident in employer:
        name = input ( 'Введите имя:' )
        cab = input('Введите кабинет')
        post = input('Введите должность')
        entry = Class_Employer.Employer(name,ident,cab,post)
        employer_dict[ident] = entry
        print ('Информация обновлена.')
    else:
        print ('Это имя не найдено. ')
        

def delete(employer_dict):
    ident = input ( 'Введите номер: ' )
    if ident in employer:
        del employer_dict[ident]
        print ('Запись удалена. ')
    else:
        print('Этo номер не найден.')        


def save_contacts(employer_dict):
    file_off = open('empl.dat','wb')
    pickle.dump(employer_dict,file_off)
    file_off.close()
def main():
    employer_dict = load_employers()
    
    choice = 0
    
    while choice != QUIT:
        choice = get_menu_employer()
        if choice == LOOK:
            look(employer_dict)
            
        elif choice == ADD:
            add(employer_dict)
            
        elif choice == CH:
            change(employer_dict)
            
        elif choice == DEL:
            delete(employer_dict)
            
    save_contacts(employer_dict)
main ()
    

    
        
    
    
            
        
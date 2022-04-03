#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:52:16 2021

@author: yamamotod
"""

import Class_Employer
import pickle

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
            #file_empl.write(my_obj)
            pickle.dump(dictin,file_empl)
            print('Файл записан')
employer()



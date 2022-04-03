#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:16:50 2021

@author: yamamotod
"""


"""
Напишите класс под названием
Pet (Домашнее животное), который должен иметь приве­
денные ниже атрибуты данных:
• _ name (для имени домашнего животного);
• _animal_type (для типа домашнего животного; например, это может быть 'собака',
'кот' и 'птица');
•
_ age (для возраста домашнего животного).
Класс Pet должен иметь метод
_ ini t _ (),
который создает эти атрибуты. Он также
должен иметь приведенные ниже методы:
• метод set _ name ()
• метод set_animal_type ()
• метод set_age ()
• метод get _ name ()
• метод get _ animal _ t
• метод get_age ()
присваивает значение полю
присваивает значение полю
присваивает значение полю
возвращает значение полю
уре
()
_ name;
_age;
_ name;
возвращает значение полю
возвращает значение полю
_animal_type;
_ animal _ t уре;
_age.
После написания данного класса напишите программу, которая создает объект класса и
предлагает пользователю ввести имя, тип и возраст своего домашнего животного. Эти
данные должны храниться в качестве атрибутов объекта. Примените методы-получатели,
чтобы извлечь имя, тип и возраст домашнего животного и показать эти данные на экране.
"""

class Pet:
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    def set_name(self,name):
        self.__name = name
        
    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type
        
    def set_age(self,age):
        self.__age = age
        
    
    def get_name(self):
        return self.__name
        
    def get_animal_type(self):
        return self.__animal_type
        
    def get_age(self):
        return self.__age

    
        
        
    














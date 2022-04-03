#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:28:48 2021

@author: yamamotod
"""
###############################################################
# Пример Композиции ООП  связка объекта с несколькими классами и
# их методами и атрибутами через объекты
##############################################################

class Employer:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
           return self.__name
    def __str__(self):
        return f"{self.__name}"
        

class Position:
    def __init__(self,pos):
        self.__pos = pos 
    def Proba(self):
        print(f'Выводим на печать связку объекта human  класса Agg \
и метода класса Position.')
        
    def get_pos(self):
           return self.__pos
    def __str__(self):
        return f"{self.__pos}"
      
class Agg:# Класс композиции агрегатор
    def __init__ (self,E,P):
        self.E = E
        self.P = P
  
        
    
        
E = Employer('Заратустра')
P = Position('Философ')

print(E)# вывод объекта через метод __str__
print(P)# вывод объекта через метод __str__

human = Agg(E,P)#  объект human привязываю к классу Agg
#с аргументами объектов оcтальных классов

print(human.P.Proba())# вывод на печать связки объекта human с  методом Proba
#  оюъекта P  класса Position


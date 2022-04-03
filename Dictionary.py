#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:33:05 2022

@author: yamamotod
"""


#value = d[key] -- извлечение элемента по ключу.
#
#d[key] = [value] -- добавление элемента (элемент является списком [ ]).


#Напишите функцию update_dictionary(d, key, value), 
#которая принимает на вход словарь d d d и два числа: key key key и value value value.
#
#Если ключ key key key есть в словаре d d d, 
#то добавьте значение value value value в список, 
#который хранится по этому ключу.
#Если ключа key key key нет в словаре, 
#то нужно добавить значение в список 
#по ключу 2∗key 2 * key 2∗key. 
#Если и ключа 2∗key 2 * key 2∗key нет,
# то нужно добавить ключ 2∗key 2 * key 2∗key 
# в словарь и сопоставить ему список из переданного элемента [value] [value] [value].
#Требуется реализовать только эту функцию, кода вне её не должно быть.

d = {}
def update_dictionary(d,key,value):
    if key in d:
        d[key] = d.get(key, []) + [value]
    if  key not in d:
        if key * 2 in d:
            d[key * 2] += [value]
        if key * 2 not in d:
            d[key * 2] = [value]
    
            
        
        
#        if value >0:
#            b = [v for v in range(1,value+1)]
#            d[2]= b
#        else:
#            a= [v for v in reversed(range(value,0))]
#            d[2]= a
#
#    if key in d:
#        d[key] = d.get(key, []) + [value]
#    
#    if key not in d:
#        d[2]= [value]
    
    
    
print(d)
print(update_dictionary(d,1,-1))
print(d)
print(update_dictionary(d,2,-2))
print(d)
print(update_dictionary(d,1,3))
print(d)
        



        
        
        
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:23:39 2021

@author: yamamotod
"""


import Pet_class

def main():
    name = 'ПУШОК'
    types = 'КОШКА'
    age = 1
    for i in range(10):
       My_pet = Pet_class.Pet(name,types,age)
       My_pet.set_age(age + 1)
       age += 1
       
       print(f'Имя: {My_pet.get_name()}')
       print(f'Тип: {My_pet.get_animal_type()}')
       print(f'Возраст: {My_pet.get_age()}')
    
    
main()
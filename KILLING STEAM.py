#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:21:46 2021

@author: yamamotod
"""

#
#Убийца steam
traffic = int(input('Введите объем приложения'))
speed = int(input('Ведите скорость соединеия'))
 
for sec,load in enumerate(range(speed, traffic, speed),1):# выводим значения индекса\
    # само значение скорости с шагом по скорости через enumerate,\
    # распаковыаем в 2 перменные
#    print(sec,load) # печать не обязательно
    proc_per_sec = round(load / traffic * 100) #  считаем процент
    print(f"Прошло {sec} сек. Скачано {load} из {traffic} Мб ({proc_per_sec} %)")
    # через f строку с placeholderam  выводим на экран
if load < traffic:#  условие  if  когда объем трафика бужет 100%
        print(f"Прошло {sec} сек. Скачано {traffic} из {traffic} Мб (100 %)")
        


    

    
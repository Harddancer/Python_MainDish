#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:08:23 2021

@author: yamamotod
"""


import Car

def main():
    my_car = Car.Car(2019,'Skoda')
    for i in range(5):
        my_car.accelerate()
        print(f'Текущая скорость: {my_car.get_speed()}')
        if my_car.get_speed() >= 25:
            for i in range(5):
                my_car.breake()
                print(f'Текущая скорость: {my_car.get_speed()}')
        else:
            None
        
main()
    
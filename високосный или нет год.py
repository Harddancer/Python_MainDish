#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 17:45:51 2022

@author: yamamotod
"""

"""
Определить, является ли год, который ввел пользователем, високосным или
невисокосным   .
"""
import unittest

def leap_year(year:int):
    #year = int(input('Введите год'))
    if year % 400 == 0:
        print(f"Год {year} високосный")
        return (f"Год {year} високосный")
    elif year % 100 == 0 and year % 400 != 0:
        print(f"Год {year} невисокосный")
        return (f"Год {year} невисокосный")
    elif year % 4 == 0:
        print(f"Год {year} високосный")
        return (f"Год {year} високосный")
    else:
        print(f"Год {year} невисокосный")
        return (f"Год {year} невисокосный")
    
class Testyear(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(leap_year(2022),f"Год 2022 невисокосный")
        self.assertEqual(leap_year(2000),f"Год 2000 високосный")
      
if __name__ == '__main__': # Main module 
   unittest.main()

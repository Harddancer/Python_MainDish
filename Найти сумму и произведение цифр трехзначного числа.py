#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:16:23 2022

@author: yamamotod
"""

"""
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь   .'''
"""
import unittest
def summ_mul(num:str):
    summa = 0
    multy = 1
    for i in num:
        summa += int(i)
        multy *= int(i)
    print(f"Сумма цифр числа {num}: {summa}, произведение: {multy}")
    return summa,multy



class Testnumbers(unittest.TestCase):
    def test_sum_mul_numbers(self):
        num = input('Введите число: ')
        self.assertEqual(summ_mul(num),(6,6))
      
if __name__ == '__main__': # Main module 
   unittest.main()
     
       

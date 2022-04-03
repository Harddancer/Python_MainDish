#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:30:30 2022

@author: yamamotod
"""

"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме
цифр. Вывести на экран это число и сумму его цифр.'''
"""
import unittest

def sum_numbers(numbers:list)->int:
    summa = 0
    for i in numbers:
        summa += int(i)
    return summa



def mains(n:list)-> int:
    maximus_summa = 0
    for i in n:
        if sum_numbers(i) > maximus_summa:
            maximus_number = i
            maximus_sum = sum_numbers(i)
    print(f'{maximus_number} сумма цифр - {maximus_sum}')
    return maximus_number,maximus_sum
            



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(('765489',39), mains(['765489']))
        self.assertEqual(('12345',15), mains(['12345']))
      
     
if __name__ == '__main__':
    unittest.main()

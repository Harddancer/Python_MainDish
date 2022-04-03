#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:03:31 2022

@author: yamamotod
"""
import unittest

def desc_number(n:int):
    itog =0
    while n > 0:
        d = n % 10
        n = n // 10
        itog = itog * 10
        itog = itog + d 
 
    print(f'Обратка:, {itog}')
    return itog   



class Test_n(unittest.TestCase):
    def test_n(self):
        self.assertEqual((321), desc_number(123))
        self.assertEqual((987654321), desc_number(123456789))
      
     
      

if __name__ == '__main__':
    unittest.main()

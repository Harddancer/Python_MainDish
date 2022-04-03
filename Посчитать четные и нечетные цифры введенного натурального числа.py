#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:18:34 2022

@author: yamamotod
"""

"""
Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import unittest

def numbers(n:int):
    l1 = [i for i in range(0,len(str(n))) if i%2 == 0]
    l2 = [i for i in range(0,len(str(n))) if i%2 != 0]
    print (f'Четных чисел {len(l1)},Не четных чисел{len(l2)}')
    return len(l1),len(l2)
numbers(34560)
        
class Test_n(unittest.TestCase):
    def test_n(self):
        self.assertEqual((3,2), numbers(34560))
        self.assertEqual((4,4), numbers(68426333))
      
     
      

if __name__ == '__main__':
    unittest.main()

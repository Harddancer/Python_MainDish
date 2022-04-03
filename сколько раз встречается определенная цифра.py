#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:57:48 2022

@author: yamamotod
"""


"""
Посчитать, сколько раз встречается определенная
цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра,
которую необходимо посчитать, задаются вводом с клавиатуры.
"""
import unittest
def count_number(l:list,m:int):
    count = 0
    for i in l:
        if i == m:
            count +=1
        else:
            None
    print(count)
    return count
count_number([1,1,1,1,1,23,4,5,5,6],1)
        
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual((5), count_number([1,1,1,1,1,23,4,5,5,6],1))
        self.assertEqual((2), count_number([1,1,23,-4,-4,5,5,6],-4))
      
     
if __name__ == '__main__':
    unittest.main() 
 

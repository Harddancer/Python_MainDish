#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:20:23 2022

@author: yamamotod
"""

"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят и сколько между ними находится букв.'''
"""
import unittest


def letters(val:str) -> tuple:
    l1, l2 = [x.upper() for x in val.split()]
    list_l = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    id_l1 = list_l.index(l1) + 1
    id_l2 = list_l.index(l2) + 1
    between_l = abs(id_l1 - id_l2) - 1
    print(f"Позиции букв в алфавите {id_l1}, {id_l2}.\n"
          f"Между ними находится букв: {between_l}.")
    return id_l1, id_l2, between_l


class Test_Letters(unittest.TestCase):
    def test_letters(self):
        self.assertEqual((4, 6, 1), letters('d f'))
        self.assertEqual((15, 23, 7), letters('o w'))
     
      

if __name__ == '__main__':
    unittest.main()

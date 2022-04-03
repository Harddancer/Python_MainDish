#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:15:26 2022

@author: yamamotod
"""


lst = [10, 5, 8, 3]

def modify_list(lst:list):
    for el in lst[:]:
        if el % 2 != 0:
            lst.remove(el)
        if el % 2 == 0:
            lst.remove(el)
            lst.append(el//2)
  
        

        

modify_list(lst)
print(lst)               # [5, 4]
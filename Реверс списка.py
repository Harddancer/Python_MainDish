#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:17:45 2022

@author: yamamotod
"""


a = input('Элементы через пробел: ')
a = a.split()
a = [int(i) for i in a]
for i in range(len(a)//2):
    b = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = b
#a.reverse()
#a = a[::-1]
print(a)

a = [1,2,3,4,5,6]
a = a[::-1]
print(a)
print(a.reverse())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:05:55 2022

@author: yamamotod
"""

"""
Вставка элемента в произвольное место массива
"""
a = []
N = 5
for i in range(N):
    num = int(input())
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))

a.insert(j - 1, num)

print(a)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:49:26 2022

@author: yamamotod
"""


"""
Суммы строк и столбцов матрицы
"""
from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
        print(b[j], end='')
    a.append(b)
    print('   |', sum(b))

for i in range(M):
    print(" --", end='')
print()

for i in range(M):
    s = 0
    for j in range(N):
        s += a[j][i]
    print(s, end='')
print()
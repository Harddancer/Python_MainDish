#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:33:14 2022

@author: yamamotod
"""


"""
В массиве случайных целых
 чисел поменять местами минимальный
 и максимальный элементы
"""
import random
def m_func():
    m = []
    for i in range(random.randint(0,30)):
        m.append(i)
 
    maxx = m[0]
    for ele in m:
        if ele > maxx:
                maxx = ele
    minn = m[0]
    for elem in m:
        if elem < minn:
                minn = elem 
                m[maxx] = m[minn]
    print(m)
    m[maxx], m[minn] = m[minn],m[maxx]
    print(m)
m_func()
    

    

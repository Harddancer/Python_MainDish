#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:45:19 2022

@author: yamamotod
"""

a = list(map(int,input().split()))
x = int(input())
for i,v in enumerate(a):
    if x not in a:
        print('Отсутствует')
        break
    if x == v:
        print(i, end = ' ')
   
        
        
#5 8 2 7 8 8 2 4
#8
    
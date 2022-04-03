#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:23:25 2022

@author: yamamotod
"""


"Бинарный поиск,высота деерева"
n = int(input())
parrents = list(map(int, input().split()))
h = [-1] * n
max_hight = -1
for i in range(n):
    hight = 1
    next = parrents[i]
    if h[i] == -1:
        while next != -1:
            if h[next]!= -1:
                hight += h[next]
                break
            hight += 1
            next = parrents[next]
    if h[i] == -1:
        h[i] = hight
    max_hight = max(max_hight,h[i])
print(max_hight)
        
    
#10
#    9 7 5 5 2 9 9 9 2 -1
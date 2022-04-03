#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:29:37 2022

@author: yamamotod
"""


s = 0
b = []
while True:
     a = int(input())
     s += a
     b.append(a**2)
     if s == 0:
        print(sum(b))
        break



#1
#-3
#5
#-6
#-10
#13
#4
#-8

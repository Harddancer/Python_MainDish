#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:09:36 2022

@author: yamamotod
"""


#a = int(input())
#b=0
#if a ==0:
#    print(0)
#else: 
#    while a != 0:
#        b +=a
#        a = int(input())
#        if a == 0:
#            print(b)
            
i = 0
s = 0
while i < 10:
    i = i + 1
    print(i,'i1')
    s = s + i
    print(s,'s')
    if s > 15:
        break
    i = i + 1
    print(i,'i2')



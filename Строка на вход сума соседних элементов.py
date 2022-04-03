#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:42:14 2022

@author: yamamotod
"""

a = list(map(int,input().split()))
b = len(a)
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)-1):
        print(a[i+1]+a[i-1],end = ' ')
    else:
        print(a[-2] + a[0])
        


    
    
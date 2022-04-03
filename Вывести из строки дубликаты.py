#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:16:58 2022

@author: yamamotod
"""

def str_dublicat(a:list)->str:
    a = sorted(a)
    b = [] * len(a)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            b.append(a[i])
    print(" ".join(map(str, list(set(b)))))

str_dublicat(list(map(int,input().split())))

    
 
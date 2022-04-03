#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:22:32 2022

@author: yamamotod
"""


a,b,c = map(int, input().split())
maxx = a
if b > maxx:
    maxx = b
if c > maxx:
    maxx = c
minn = a
if b < minn:
    minn = b
if c < minn:
    minn = c
other =(a+b+c)-(maxx+minn)
print(maxx,minn,other,sep='\n' )
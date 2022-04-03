#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:44:28 2021

@author: yamamotod
"""


m1 =[]
m2 = []

a = [[1,2],[3,4], [5,6]]

m1 = [ a[i][1] for i,row in enumerate(a)]
m2 = [ a[i][0] for i,row in enumerate(a)]
itog = []
print(m1,m2)
    

for x, y in zip(m1,m2): 
   itog += [x+y]

if len(m1) > len(m2):
   itog += m1[len(m1)-len(m2)+1:]
elif len(m1) < len(m2):
   itog += m2[len(m2)-len(m1)+1:]

print(itog) 
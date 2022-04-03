#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 00:51:39 2022

@author: yamamotod
"""


string = input().split( )
s = set(string)
print(s)
for i in s:
    print(i,string.count(i))
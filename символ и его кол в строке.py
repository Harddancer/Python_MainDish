#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 13:37:25 2022

@author: yamamotod
"""




s = input().lower()
l=len(s)

cnt=1
for i in range(l):
    if i==(l-1):
        print(s[i]+str(cnt),end='')
    else:
        if s[i]==s[i+1]:
            cnt=cnt+1
        else:
            print(s[i]+str(cnt),end='')
            cnt=1
            
            

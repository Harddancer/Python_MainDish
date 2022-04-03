#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 13:37:25 2022

@author: yamamotod
"""


#s = input().lower()
#print(((s.count('c') + s.count('g'))/ len(s)) * 100)
#
#
#s = 'abcdefghijk'
#s[3:6]
#s[:6]
#s[3:]
#s[::-1]
#s[-3:]
#print(s[:-6])
#print(s[-1:-10:-2])

s = input().lower()
l=len(s)
print(len(s)-1)
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
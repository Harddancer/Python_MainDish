#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:52:44 2022

@author: yamamotod
"""
import time
start = time.time()
def fact(n):
    if n == 1:
       
        return 1
    
    else:
        
        return n*fact(n-1)
end = time.time()    
print(fact(7))
print(end-start)        
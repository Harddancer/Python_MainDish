#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:24:52 2022

@author: yamamotod
"""


" Class Min Stack"
class MinStack():
    def __init__(self):
        self.stack = []
    def push(self,val:int):
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))
    def pop(self)-> None:
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def getmin(self):
        return self.stack[-1][1]
    
            
            
        
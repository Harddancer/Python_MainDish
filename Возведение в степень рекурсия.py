#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:00:56 2022

@author: yamamotod
"""


"""
Возведение в степень важно
"""
class Solution:
    def ispowertwo(self,n:int)-> bool:
        if n ==1:
            return True
        if n % 2 != 0 or n == 0:
            return False
        return self.ispowertwo(n / 2)
    
test = Solution()
print(test.ispowertwo(1))
print(test.ispowertwo(80))
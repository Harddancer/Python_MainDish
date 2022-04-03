#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:30:47 2022

@author: yamamotod
"""


"""
Вывести строку в обратном порядке при использовании массива ЦИКЛ
"""
def revers_string(n:str):
    m = []
    for i in range(0,len(n)):
        m.append(n[len(n)-i-1])
    print( ' '.join(m))

revers_string('adf')        

"""
Вывести строку в обратном порядке при использовании строки in place ЦИКЛ
"""
def revers_string(n:str):
    for i in range(0,len(n)):
        print(n[len(n) - i-1], end = ' ')
    

revers_string('ert') 

"""
Вывести строку в обратном порядке при использовании строки in place РЕКУРСИЯ
"""

def recursiv_revers_string(n:str):
    def helper(n,index):
        if index >= len(n):
            return
        helper(n,index+1)
        print(n[index], end = '')
        
    helper(n,0)
recursiv_revers_string('qwertyuiop')    
    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:42:14 2022

@author: yamamotod
"""
#Иначе тогда проходим циклом всю длину нашей строки за
# исключением последней итерации, её мы можем убрать
# вот таким способом - for i in range(n-1). Каждую итерацию мы принтуем s[i+1]+s[i-1],end=" ". По завершению 
#цикла выводим последнюю часть условия "иначе", а именно выводим последний элемент s[-2]+s[0]
#a = [1 2 3 4 5]
a = list(map(int,input().split()))
b = len(a)
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)-1):
        print(a[i+1]+a[i-1],end = ' ')
    else:
        print(a[-2] + a[0])
        


    
    
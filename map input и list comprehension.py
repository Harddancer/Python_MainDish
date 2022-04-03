#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:45:19 2022

@author: yamamotod
"""

a, x = list(map(int,input().split())),int(input())

for i,v in enumerate(a):
    if x not in a:
        print('Отсутствует')
        break
    if x == v:
        print(i, end = ' ')
   
l, n = [int(i) for i in input().split()], int(input())
print(*[x for x in range(len(l)) if l[x]==n] if n in l else ["Отсутствует"])        
#if n in l- первое что проверяется есть ли n в l, 
# если условие выше верно, то проверятся условие слева, перебираем индекс в списке l если
# x значение равно n печатаем
# в противном случае сразу без выполнения перебора выполняется условие else справа от  if in l

        
#5 8 2 7 8 8 2 4
#8
    
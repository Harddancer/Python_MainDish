#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:20:07 2022

@author: yamamotod
"""
# Sample Input:
#
#a3b4c2e10b1
#
#Sample Output:
#
#aaabbbbcceeeeeeeeeeb
import os
from pathlib import Path
print(Path.cwd())

string = ''
print(os.getcwd())
with open('dataset_3363_2.txt','r') as f:
   l = f.readline()
for i in range(len(l)-1):
    if l[i+1].isdigit():
        #print(l[i]*int(l[i+1]), end = '')
        string += l[i]*int(l[i+1])
        
    if l[i+1].isdigit() and l[i+2].isdigit():
        #print(l[i]*int(l[i+1] + l[i+2]), end = '')
        string += l[i]*int(l[i+1] + l[i+2])
print(string)
      

    
with open('output2.txt','w') as f2:
    f2.writelines(string)
    
    
a = input()

b = []

for i in range(len(a)):

   if a[i] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':

       b+=a[i]

       a=a[:i]+"!"+a[i+1:]

c=a.split('!')[1:]

for i in range(len(b)):

   print(b[i]*int(c[i]), end="")    
    
### РЕШЕНИЕ
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j    
    
#Первый символ - гарантированно буква.
#Перебираем все последующие, 
#пока они цифровые или пока не достигнут конец строки.
#После внутреннего цикла j либо указывает на следующую букву,
# либо на конец строки. В обоих случаях между s[i] и s[j] - цифры,
# составляющие нужное нам число повторов символа s[i].
#Печатаем символ нужное число раз, присваиваем 
#i индекс следующей буквы для новой итерации цикла.    
    
    
    
    
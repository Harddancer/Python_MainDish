#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:02:45 2022

@author: yamamotod
"""
#Выведите таблицу размером n×n n \times n n×n, заполненную числами
# от 1 1 1 до n2 n^2 n2 по спирали, выходящей из левого верхнего угла 
#и закрученной по часовой стрелке, как показано в примере (здесь n=5 n=5 n=5):
n = int(input())
array_output = [[0 for j in range(n)] for i in range(n)]
#print(array_output)
x1,y1 = 0,0
x2,y2 = 1,0

for i in range(1,n**2+1):
    array_output[x1][y1] = i
    cx,cy = x1+x2,y1+y2
    if 0<=cx<n and 0<=cy<n and array_output[cx][cy] == 0:
       x1 = cx
       y1 = cy
    else:
       x2,y2 = -y2,x2
       x1,y1 = x1+x2, y1+y2
#print(array_output)
        
    
n = range(len(array_output))
for y in n:
    for x in n:
        print (array_output[x][y],end=' ')
    print()    
    
   
    



    


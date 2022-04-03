#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:22:44 2022

@author: yamamotod
"""
count, a1, b1, c1 = 0, 0, 0, 0
with open('dataset_3363_4.txt', 'r') as inf,open('dataset_3363_4_output.txt','w') as file_w:
    for line in inf:
        line = line.strip().split(';')
        a, b, c = int(line[1]), int(line[2]), int(line[3])
        a1 += a
        b1 += b
        c1 += c
        count += 1
        print((a+b+c)/3)
        aver_marks = (a+b+c)/3
        file_w.write(str(aver_marks) + '\n')
    file_w.write(str(a1/count)  + ' '+ str(b1/count)  + ' '+ str(c1/count))
print((a1/count), (b1/count), (c1/count))

    
 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:51:44 2022

@author: yamamotod
"""


with open('dataset_3363_4.txt','r') as file:
    file_read = file.readlines()

with open('dataset_3363_4_output.txt','w') as file_w:
    l1 = []
    l2 = []
    l3 = []
    for line in file_read:
        line = line.strip().split(';')
#        print(line)
        marks = 0
        count = 0
        for l in line[1:]:
            marks += int(l)
            count +=1
            aver_marks = marks/(count)
            
            if line[1:].index(l) == 0:
                l1.append(int(l))
            if line[1:].index(l) == 1:
                l2.append(int(l))
            if line[1:].index(l) == 2:
                l3.append(int(l))
        print(aver_marks)
        file_w.write(str(aver_marks) + '\n')
    print(sum(l1)/len(l1),sum(l2)/len(l2),sum(l3)/len(l3))
    file_w.write(str(sum(l1)/len(l1))  + ' ' \
                 + str(sum(l2)/len(l2))  + ' ' \
                 + str(sum(l3)/len(l3)))
    
    
    

  


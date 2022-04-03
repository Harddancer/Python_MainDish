#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:31:03 2021

@author: yamamotod
"""

#
#d = {'a':1,'b':2,'c':3}
#print(d)
#if 'a' in d:
#    del d['a']
#print(d)

#s =set(['a','b','c'])
#s =set('abcrty')
#d = set('dddddddavb')
#n = s-d
#print(n)
#print(s)
#
#my_set = set([10,20,30])
#print(my_set)
#1
#=============
lesson = ['CS101','CS102','CS103']
cabinet = [324,5665,876]
names = ['Rodrigo,Penelopa,Faust']
d= dict(zip(lesson,cabinet))
d2 = {key : [value] for key, value in d.items()}
d2["CS101"].append("Rodrigo")
d2["CS102"].append("Penelopa")
d2["CS103"].append("Faust")
d2["CS103"].append("Faust1")
print(d2)



    





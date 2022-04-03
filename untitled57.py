#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:31:36 2022

@author: yamamotod
"""


def insertion_sort(array_to_sort):
    a = array_to_sort
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
            a[j] = v
#    print(a)
    return a
ary = [54,1,2,3,52,3,1,2,3,5,3,67,3,2,543]
print(insertion_sort(ary))
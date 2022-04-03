#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:27:59 2022

@author: yamamotod
"""


def selection_sort(array_to_sort):
    a = array_to_sort
    for i in range(len(a)):
        idx_min = i
        for j in range(i+1, len(a)):
            if a[j] < a[idx_min]:
                idx_min = j
                tmp = a[idx_min]
                a[idx_min] = a[i]
                a[i] = tmp
    return a
ary = [0,3,5,1,2,3,5,4,2,34,43,24]
print(selection_sort(ary))
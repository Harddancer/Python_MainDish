#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:43:38 2022

@author: yamamotod
"""


import random
def qsort_inplace(lst, start=0, end=None):

    def subpart(lst, start, end, pivot_index):
        lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
        pivot = lst[start]
        x = start + 1
        y = start + 1
        while y <= end:
            if lst[y] <= pivot:
                lst[y], lst[x] = lst[x], lst[y]
                x += 1
            y += 1
        lst[start], lst[x - 1] = lst[x - 1], lst[start]
        return x - 1
    
    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return

    pivot_index = random.randint(start, end)
    x = subpart(lst, start, end, pivot_index)
    qsort_inplace(lst, start, x - 1)
    qsort_inplace(lst, x + 1, end)

ary = [54,1,2,3,52,3,1,2,3,5,3,67,3,2,543]
print(qsort_inplace(ary))
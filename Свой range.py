#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 22:37:25 2022

@author: yamamotod
"""


def cool_range(start, stop, inc):
    x = start
    while x < stop:
        yield x
        x += inc

for n in cool_range(1, 5, 0.5):
    print(n)
# 1
# 1.5
# ...
# 4.5

print(list(cool_range(0, 2, 0.5)))
# [0, 0.5, 1.0, 1.5]
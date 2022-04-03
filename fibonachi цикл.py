#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:10:53 2022

@author: yamamotod
"""


n = int(input())


def fibonacci(n):
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


print(*fibonacci(n))
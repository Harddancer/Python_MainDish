#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:27:17 2022

@author: yamamotod
"""


def main () :
    print('Пepвыe 10 последовательности Фибоначчи:')
    for number in range(1, 5):
        print(fib(number))
# Функция fib возвращает n-e число
# последовательности Фибоначчи.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

main ()
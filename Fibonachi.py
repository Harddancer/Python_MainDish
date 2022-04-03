# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:34:12 2021

@author: mvandron
"""
# генератор списка Фибоначи
def fin(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


ln = int(input('How long? '))
print(list(fin(ln))) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]

"""

# Функция
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

# Рекурсия
def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

element = input('Введите номер искомого элемента : ')
element = int(element)
value = fibonacci(element)
print(str(element)+' элемент последовательности равен ' + str(value))

# Фибоначи 
def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for i in range(5):
    print(next(gen))
"""
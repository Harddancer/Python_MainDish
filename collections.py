#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:54:07 2022

@author: yamamotod
"""


import collections
 
company = collections.namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4', 'y'])
companys = []
q = int(input("Введити кол-во компаний: "))
total = 0
for i in range(q):
    name = input(f"Название {i+1}-ого предприятия: ")
    q1 = int(input("Прибыль за 1 квартал: "))
    q2 = int(input("Прибыль за 2 квартал: "))
    q3 = int(input("Прибыль за 3 квартал: "))
    q4 = int(input("Прибыль за 4 квартал: "))
    y = q1 + q2 + q3 + q4
    total += y
    companys.append(company(name=name, q1=q1, q2=q2, q3=q3, q4=q4, y=y))
total_avg = total / q
print(f"Предприятия с прибылью выше средней {total_avg}: ")
for company in companys:
    if company.y >= total_avg:
        print(company.name)
print(f"Предприятия с прибылью неже средней {total_avg}: ")
for company in companys:
    if company.y < total_avg:
        print(company.name)
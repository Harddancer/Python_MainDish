#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:04:12 2021

@author: yamamotod
"""


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

#Викторина со столицами. Напишите программу, которая создает словарь, содержащий
#в качестве ключей названия американских штатов и в качестве значений их столицы.
#(Список штатов и соответствующих им столиц можно найти в Интернете.) Затем про­
#грамма должна провести викторину, случайным образом выводя название штата и пред­
#лагая ввести его столицу. Программа должна провести подсчет количества правильных
#и неправильных ответов. 

from random import choice
with open('Stats.txt','r') as file:
    dic = {}
    for line in file:
        d = line.rstrip('\n').split(' ')
        dic[d[0]] = d[-1]

print('*' * 43)    
print('!!!Викторина на знание столиц штатов США!!!')
print('*' * 43)   
print('Вы хотите играть? Да или Нет')
user =input('Введите Ваш ответ  ')

good = 0
bad = 0
while user.capitalize() == 'Да':
   
    k = choice(list(dic.keys()))
    capital = input(f'Назовите столицу штата  {k} ?')
    if capital  == dic.get(k):
        print(f'Правильно')
        good += 1
    else:
        print(f'Увы и Ах')
        bad += 1
    user =input('Вы хотите продолжить?')
    if user == 'Да':
        continue
    elif user.capitalize() == 'Нет':
        print(f'Правильных ответов {good}, не правильных ответов {bad}')
        break
    
    
    
    
    



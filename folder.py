# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:03:17 2021

@author: mvandron
"""
"""
import os 
import pandas as p

print(os.getcwd())
print(os.chdir('/home/yamamotod/Рабочий стол/GeekBrains'))
print(os.getcwd())
os.chdir('Python_mybook')
if not os.path.isdir('folder'):
    print('Нет такой папки')
print(os.getcwd())
print(os.listdir())
os.chdir('my_project')
print(os.getcwd())
new_file = open('numbers', 'w')
for n in range(1,10):
    new_file.write('новая строка\n')
new_file.close()
print('Файл записан')
with open('numbers') as new_file:
    print(new_file.read())"
"""    
"""
def data():
    with open ('data.txt', 'w') as file:
        for n in range(1,7):
            file.write('ого какая строка\n')
    
file =  open ('data.txt', 'r') 
line = file.readline()
while line != '':
    line = line.rstrip('\n')
    print(line)
    line = file.readline()
file.close()
print('Файл прочитан')

data()        
"""  



"""
if not os.path.isdir("folder"):
     os.mkdir("folder")
     
os.chdir('.cisco')
cwd = os.getcwd()
print(cwd)
os.chdir('..')
cwd = os.getcwd()
print(cwd)
os.chdir('folder')
#os.makedirs("nested1/nested2/nested3")
with open("text.txt") as text_file:
    text_file = open("text.txt", "w")
    text_file.write("Это текстовый файлoiuytre\n")
    text_file = open("text.txt", "a")
    text_file.write("добавление")
    text_file = open("text.txt", "r")
    print(text_file.readline())
"""




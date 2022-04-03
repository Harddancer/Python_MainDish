#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 01:03:56 2021

@author: yamamotod
"""


 Python и чтение из excel с записью в mysql как ускорить?
Задавал уже вопрос про оптимизацию. Придумал такой пример ради интереса:
прочитать 500 тыс.строк.(инфа о пользователях) из excel и сохранить в mysql.
Задача в данном случае вымышленная, но, думаю, такие возникают.
Скрипт отрабатывает за 260 сек.

import mysql.connector
import openpyxl
import time

start = time.time()
conn = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='exceltest')
cursor = conn.cursor()
wb = openpyxl.load_workbook('kniga.xlsx')
sheet = wb.active
for i in range(2, 500002): #Читаем со 2-й строки (1-я заголовок)
    nm = sheet[f'A{i}'].value #id
    name = sheet[f'B{i}'].value #имя
    fam = sheet[f'C{i}'].value #фамилия
    otch = sheet[f'D{i}'].value #отчество
    vod_pr = sheet[f'E{i}'].value #Водительские права(Есть/Нет)
    sem_pol = sheet[f'F{i}'].value #Семейное положение(Да/Нет)
    prof = sheet[f'G{i}'].value #Профессия
    cursor.execute("""insert into table1(id, name, fam, otch, vod_pr, sem_pol, prof)
                  values(%s, %s, %s, %s, %s, %s, %s)""", (nm, name, fam, otch, vod_pr, sem_pol, prof))
conn.commit()
cursor.close()
conn.close()
end = time.time()
print(end-start)


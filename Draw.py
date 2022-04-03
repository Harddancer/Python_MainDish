# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:22:09 2021

@author: mvandron
"""
from PIL import  Image # модули бибилиотеки pillow  для изображения
from PIL import ImageDraw # модуль для обработки изобоажения
imageFON = Image.new("RGBA", (400,400), (0,0,0,0))# создаем фон, размеры и прозрачность
draw = ImageDraw.Draw(imageFON)# создаем объект ImageDraw и передаем ему рисунок
print ('Привет,Чувак!')
variant = int(input('Что ты хочешь нарисовать? Круг-жми 1,Квадрат 2'))
if variant == 1:#  первое условие
     r = int(input('Введите радиус круга'))
     draw.ellipse((0, 0, r, r), fill='red', outline=(0, 0, 0))
     imageFON.show() #  открытия файла с рисунком 
elif variant == 2:#  второе условие
     h = int(input('Введите высоту прямоугольника'))
     w = int(input('Введите ширину прямоугольника'))
     draw.rectangle((0, 0, h, w), fill='green', outline=(0, 0, 0))
     imageFON.show() #  открытия файла с рисунком 
else:
     print('Не верное число')
  
  

 
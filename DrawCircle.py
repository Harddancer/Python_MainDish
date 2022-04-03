# -*- coding: utf-8 -*-
"""ыы
Created on Tue Jun 15 13:33:03 2021

@author: mvandron
"""
from PIL import  Image,ImageColor # модули бибилиотеки pillow  для изображения и цвета
from PIL import ImageDraw# модуль для обработки изобоажения
imageFON = Image.new("RGBA", (400,400), (0,0,0,0))# создаем фон, размеры и прозрачность
draw = ImageDraw.Draw(imageFON)# создаем объект ImageDraw и передаем ему рисунок
draw.ellipse ((0,0,180,180), fill=ImageColor.getrgb("yellow"), outline=ImageColor.getrgb("black"),width=10)# лицо
draw.ellipse ((50, 40, 70, 60), fill=ImageColor.getrgb("black"), outline=ImageColor.getrgb("black"))# глаз
draw.ellipse ((100, 40, 120, 60), fill=ImageColor.getrgb("black"), outline=ImageColor.getrgb("black"))#глаз
draw.arc((30, 30,140,140),0,180, 'black', width=10)# рисуем рот
imageFON.show()#  открытия файла с рисунком






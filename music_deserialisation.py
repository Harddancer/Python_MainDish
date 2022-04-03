# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:23:27 2021

@author: mvandron
"""
import pickle,json
#Десериализация  
sound = {
    'name':'AC/DC',
    'album':'The Razors Edge',
    'year':'1990',
    'tracks':['Thunderstruck', 'Moneytalks'],
    }  
with open('new_sound','rb') as f:
    pickle.load(f)
    print('pickle good!')
     
with open('new_sound2','r',encoding = 'utf-8') as f:
    new_sound2 = json.load(f)
    json.load(f)
    print(type(sound))
    print('json good!')
    
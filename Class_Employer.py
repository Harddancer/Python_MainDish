#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:13:12 2021

@author: yamamotod
"""


class Employer:
    def __init__(self,name,ident,cab,post):
        self.name = name
        self.ident = ident
        self.cab = cab
        self.post = post
    
    def __str__(self):
        return f"Имя: {self.name}\n ID:{self.ident}\n Кабинет:{self.cab}\n Должность:{self.post}"
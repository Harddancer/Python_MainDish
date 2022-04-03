#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:45:42 2022

@author: yamamotod
"""


def main () :
    num1 = int(input('Bвeдитe целое'))
    num2 = int(input('Bвeдитe еще число:одно'))
    print('Наибольший общий делитель', gcd(num1,num2))
    

def gcd(x, у):
    if x % у == 0:
        return у
    else:
        return gcd(x,x % у)
main ()
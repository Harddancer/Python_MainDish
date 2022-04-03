# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:46:40 2021

@author: mvandron
"""

friend = {
    'name': 'Max',
    1: 23,
    'cars': 'Volvo'
    }
print(friend[1])


print(friend['name'])
print(friend)
print(type(friend))
print(friend['cars'])
friend ['flat'] = True
print(friend)
for key in friend.keys():
    print(key)
    print(friend[key])
    
for val in friend.items():
    print(val)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:17:12 2022

@author: yamamotod
"""



def reverseString(lists) -> None:
    def helper(lists,i,f,e):
        s = len(lists)//2
        f=0
        e=1
        if s == f:
            return
        lists[i], lists[len(lists)-e] = lists[len(lists)-e],lists[i]
        helper(lists,i+1,f+1,e+1)
        print(lists)
    helper(lists,0,0,1)
reverseString(["h","e","l","l","o"])                


def reverseString(s):
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
    helper(0, len(s) - 1)
















        
            e = 1
            f = 0
            s = len(lists)//2
            if s == f:
                return lists
            else:
               reverseString() 
                
                
               for i in range(len(lists)-1):
                   lists[i], lists[len(lists)-e] = lists[len(lists)-e],lists[i]
                   f +=1
                   e +=1
#    print(lists)
    return lists
    
                
reverseString(["h","e","l","l","o"])       
        
        
def recursiv_revers_string(n:str):
    def helper(n,index):
        if index >= len(n):
            return
        helper(n,index+1)
        print(n[index], end = '')
        
    helper(n,0)
recursiv_revers_string('qwertyuiop')        
                
                
                
                
 #Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
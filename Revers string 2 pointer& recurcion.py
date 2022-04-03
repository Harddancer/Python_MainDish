#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:17:12 2022

@author: yamamotod
"""



def reverseString(lists) -> None:
    def helper(lists,i,e):
       if i >=len(lists)//2:
            return
       lists[i], lists[len(lists)-e] = lists[len(lists)-e],lists[i]
       helper(lists,i+1,e+1)

    helper(lists,0,1)
    print(lists)
reverseString(["h","e","l","l","o"])                



    def reverseString(self, s: List[str]) -> None:
        st = len(s)//2
        f = 0
        e = 1
        for i in range(len(s)-1):
            if st !=f:
                s[i], s[len(s)-e] = s[len(s)-e],s[i]
                f +=1
                e +=1
        return s













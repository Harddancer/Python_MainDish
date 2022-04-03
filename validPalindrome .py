#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:05:09 2022

@author: yamamotod
"""



def validPalindrome(s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] == s[j]:
                i, j = i+1, j-1
            else:
                return (s[i+1:j+1] == s[i+1:j+1][::-1]) or (s[i:j] == s[i:j][::-1])
        
        return True
print(validPalindrome("abca"))



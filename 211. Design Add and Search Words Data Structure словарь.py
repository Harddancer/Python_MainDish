#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:39:33 2022

@author: yamamotod
"""


    
    
    
from collections import defaultdict
class WordDictionary:
    def __init__(self):
        self.d = defaultdict(list)
    
    def addWord(self, word):
        self.d[len(word)].append(word)
    
    def search(self, word):
        words = self.d[len(word)]
        
        for each in words:
            if each == word: return True
            for e, w in zip(each, word):
                if w == ".": continue
                if e != w: break
            else: return True
        return False

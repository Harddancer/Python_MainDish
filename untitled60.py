#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:44:46 2022

@author: yamamotod
"""


#from collections import defaultdict
class WordDictionary:
    def __init__(self):
        self.dictin = {}
    
    def addWord(self, word):
        self.dictin(len(word),[])
    
    def search(self, word):
        words = self.dictin[len(word)]
        
        for elem in words:
            if elem == word: return True
            for elem, word in zip(elem, word):
                if word == ".": continue
                if elem != word: break
            else: return True
        return False

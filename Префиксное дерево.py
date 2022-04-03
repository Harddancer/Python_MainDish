#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:57:44 2022

@author: yamamotod
"""


class TrieNode:
    def __init__(self):
     
        self.ended = False
        self.children = {}


class Trie:
    def __init__(self):
     
        self.root = TrieNode()

    def insert(self, word):
      
        current = self.root
        for word in word:
            if word not in current.children:   
                current.children[word] = TrieNode()
                current = current.children[word]

        current.ended = True

    def search(self, word):
   
        current = self.root
        for word in word:
            if word in current.children:
                current = current.children[word]
            else:
                return False

        if not current.ended:  
            return False

        return True

    def startsWith(self, prefix):
     
        current = self.root
        for word in prefix:
            if word in current.children:
                current = current.children[word]
            else:
                return False

        return True  
        
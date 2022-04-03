#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:56:01 2022

@author: yamamotod
"""


class TrieNode(object):
    """docstring for TrieNode"""
    def __init__(self):
        self.childs = dict()
        self.isWord = False
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(root, word):
            if len(word) == 0:
                return root.isWord
            elif word[0] == '.':
                for node in root.childs:
                    if dfs(root.childs[node], word[1:]):
                        return True
                return False
            else:
                node = root.childs.get(word[0])
                if node is None:
                    return False
                return dfs(node, word[1:])

        return dfs(self.root, word)
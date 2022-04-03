#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:53:01 2022

@author: yamamotod
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root: return None

        nodes_level = []
        level = [root]
        left_border = node.left
        right_border = node.right

        while level:
            for node in level:
                nodes_level.append(node)
            if child:
                for child in (left_border,right_border) :
                    level.append(child)
                
            

        for nodes in nodes_level:
            for index in range(len(nodes) - 1):
                nodes[index].next = nodes[index + 1]

        return root
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:09:55 2022

@author: yamamotod
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(TreeNode):
    def isSymmetric(root:list) -> bool:
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop()
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True 
tree = Solution
print(tree.isSymmetric([1,2,2,3,4,4,3]))
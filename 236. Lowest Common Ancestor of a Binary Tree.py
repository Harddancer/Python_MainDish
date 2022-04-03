#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:10:20 2022

@author: yamamotod
"""
"""
236. Lowest Common Ancestor of a Binary Tree
"""
#  Основное делаем через рекурсию, алгоритм
# разделя и властвуй, бинарный поиск,
# бзовый случай - если нет вершины то вернуть none, 
#если есть оба узла то вернуть их вершину.
#Если только левый есть нода возврщ ее и наоборот.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if not root: return None

        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
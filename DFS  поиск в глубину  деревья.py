#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:51:23 2022

@author: yamamotod
"""


def dfs(graph, start, visited=None):
    if visited is None:
       visited = set()
    visited.add(start)
    print(start, end = ' ')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
     
graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}
     
dfs(graph, '4')
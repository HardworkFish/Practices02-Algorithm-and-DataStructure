#!/usr/bin/env python
# Python 实现深度优先搜索
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end = " ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self, v):
        visited = [False]*(len(self.graph))
        self.DFSUtil(v, visited)
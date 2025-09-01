#!/usr/bin/env python3
from collections import deque
n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
edges = []
for _ in range(m) :
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    edges.append((u,v))
for i in range(n) :
    visited = []
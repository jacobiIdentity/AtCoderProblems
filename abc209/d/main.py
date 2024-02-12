#!/usr/bin/env python3
from collections import deque
n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1) :
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
colors = [0]+[-1]*(n-1)
que = deque()
que.append(0)
now = 0
while que :
    now = que.popleft()
    for v in graph[now] :
            if colors[v] == -1 :
                colors[v] = 1 - colors[now]
                que.append(v)
for _ in range(q) :
    c, d = map(int, input().split())
    print('Town' if colors[c-1] == colors[d-1] else 'Road')

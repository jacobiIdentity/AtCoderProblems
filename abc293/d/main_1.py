#!/usr/bin/env python3
from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n)]
degs = [0]*n
for _ in range(m) :
    a, b, c, d = input().split()
    graph[int(a)-1].append(int(c)-1)
    graph[int(c)-1].append(int(a)-1)
    degs[int(a)-1] += 1
    degs[int(c)-1] += 1
visited = [False]*n
x, y = 0, 0
for i in range(n) :
    if visited[i] :
        continue
    que = deque()
    visited[i] = True
    isCircle = True
    que.append(i)
    while len(que) > 0 :
        j = que.pop()
        if degs[j] != 2 :
            isCircle = False
        for k in graph[j] :
            if not(visited[k]) :
                que.append(k)
                visited[k] = True
    if isCircle : x += 1
    else : y += 1
print(x, y)

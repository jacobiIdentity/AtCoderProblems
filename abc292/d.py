#!/usr/bin/env python3
from collections import deque
import sys
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m) :
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
que = deque()
visited = [False]*n
for i in range(n) :
    if len(graph[i]) == 0 :
        print('No')
        exit()
for i in range(n) :
    if visited[i] : continue
    que.append(i)
    visited[i] = True
    vs = set()
    eCnt = 0
    while len(que) > 0 :
        now = que.popleft()
        vs.add(now)
        for j in graph[now] :
            eCnt += 1
            vs.add(j)
            if visited[j] : continue
            visited[j] = True
            que.append(j)
    if len(vs) != eCnt//2 :
        print('No')
        exit()
print('Yes')
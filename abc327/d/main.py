#!/usr/bin/env python3
from collections import deque
n, m = map(int, input().split())
a_m = list(map(int, input().split()))
b_m = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(m) :
    graph[a_m[i]-1].append(b_m[i]-1)
    graph[b_m[i]-1].append(a_m[i]-1)
color = [-1 for _ in range(n)]
ans = 'Yes'
for v in range(n) :
    if color[v] != -1 :
        continue
    q = deque()
    color[v] = 0
    q.append(v)
    while q :
        qv = q.popleft()
        for nextv in graph[qv] :
            if color[nextv] != -1 : 
                if color[nextv] == color[qv] :
                    print('No')
                    exit()
                continue
            color[nextv] = 1 - color[qv]
            q.append(nextv)
print('Yes')
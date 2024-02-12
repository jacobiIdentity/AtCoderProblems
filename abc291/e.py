#!/usr/bin/env python3
from collections import deque
import sys
n, m = map(int,input().split())
graph = [[] for _ in range(n)]
indeg = [0]*n
for _ in range(m) :
    x, y = map(int,input().split())
    graph[x-1].append(y-1)
    indeg[y-1] += 1
ans = [0]*n
que = deque()
for i in range(n) :
    if not(indeg[i]) : que.append(i)
cnt = 0
while que :
    if len(que) > 1 :
        print('No')
        exit()
    v = que.pop()
    cnt += 1
    ans[v] = cnt
    for vv in graph[v] :
        indeg[vv] -= 1
        if not(indeg[vv]) :
            que.append(vv)
print('Yes')
print(*ans)
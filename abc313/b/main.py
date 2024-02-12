#!/usr/bin/env python3
from collections import defaultdict, deque
import sys
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m) :
    a, b = map(lambda x:x-1,map(int, input().split()))
    graph[a].append(b)
for i in range(n) :
    isSaikyo = True
    for j in range(n) :
        if i == j : continue
        q = deque()
        q.append(i)
        visited = [False]*n
        isStronger = False
        while q :
            k = q.popleft()
            visited[k] = True
            for l in graph[k] :
                if l == j :
                    isStronger = True
                    break
                if not(visited[l]) :
                    q.append(l)
            if isStronger :
                break
        if not(isStronger) :
            isSaikyo = False
            # print(i+1, j+1)
    if isSaikyo :
        print(i+1)
        exit()

print(-1)





#!/usr/bin/env python3
import sys,copy
from collections import defaultdict
sys.setrecursionlimit(10**8)
def dfs(x,dist) :
    global ans
    visited[x] = True
    for y in d[x] :
        if visited[y] :
            ans = max(ans,dist)
            # print(x,y,dist,l)
        elif graph[x][y] == 0 :
            ans = max(ans,dist)
            # print(x,y,dist,l)
        else :
            # print(x,y,dist+graph[x][y],l)
            dfs(y,dist+graph[x][y])
    return

n,m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
d = defaultdict(list)
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
    d[a-1].append(b-1)
    d[b-1].append(a-1)
ans = 0
for i in range(n) :
    visited = [False]*n
    dfs(i,0)
print(ans)



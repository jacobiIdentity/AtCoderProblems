#!/usr/bin/env python3
from collections import deque
import sys
sys.setrecursionlimit(10**8)
def dfs(x,y) :
    stopped[x][y] = True
    visited[x][y] = True
    if x > 2 :
        tmp = 2
        for i in range(x-1, 0, -1) :
            if s_n[i][y] == '#' :
                tmp = i+1
                break
            visited[i][y] = True
        if not(stopped[tmp][y]) :
            dfs(tmp,y)
    if x < n-1 :
        tmp = n-1
        for i in range(x+1, n+1) :
            if s_n[i][y] == '#' :
                tmp = i-1
                break
            visited[i][y] = True
        if not(stopped[tmp][y]) :
            dfs(tmp,y)
    if y > 2 :
        tmp = 2
        for i in range(y-1, 0, -1) :
            if s_n[x][i] == '#' :
                tmp = i+1
                break
            visited[x][i] = True
        if not(stopped[x][tmp]) :
            dfs(x,tmp)
    if y < m-1 :
        tmp = m-1
        for i in range(y+1, m+1) :
            if s_n[x][i] == '#' :
                tmp = i-1
                break
            visited[x][i] = True
        if not(stopped[x][tmp]) :
            dfs(x,tmp)
    return
n, m = map(int, input().split())
s_n = ['*'*m]+['*'+input() for _ in range(n)]
visited = [[False]*(m+1) for _ in range(n+1)]
stopped = [[False]*(m+1) for _ in range(n+1)]
ans = 0
dfs(2,2)
for i in range(1,n+1) :
    ans += visited[i].count(True)
print(ans)

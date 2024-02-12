#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def dfs(x,y,t) :
    if 'snuke'[t%5] != s_h[y][x] :
        return
    if (x,y) in visited :
        return
    visited.add((x,y))
    # print(x,y,t)
    if x == w-1 and y == h-1 :
        print('Yes')
        exit()
    if x > 0 :
        dfs(x-1, y, t+1)
    if y > 0 :
        dfs(x, y-1, t+1)
    if x < w-1 :
        dfs(x+1, y, t+1)
    if y < h-1 :
        dfs(x, y+1, t+1)
visited = set()
h, w = map(int, input().split())
s_h = [input() for _ in range(h)]
dfs(0, 0, 0)
print('No')
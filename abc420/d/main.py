#!/usr/bin/env python3
from collections import deque
h,w = map(int,input().split())
grid = [input() for _ in range(h)]
si,sj = 0,0
gi,gj = 0,0
for i in range(h) :
    for j in range(w) :
        if grid[i][j] == "S" :
            si,sj = i,j
        if grid[i][j] == "G" :
            gi,gj = i,j
dist = [[[float("inf")]*2 for _ in range(w)] for _ in range(h)]
dist[si][sj][0]=0
que = deque()
que.append((si,sj,0))
while que : 
    r,c,s = que.popleft()
    # print(r,c,s,dist[r][c][s])
    if grid[r][c] == "G" :
        print(dist[r][c][s])
        exit()
    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)] :
        if not(0<=r+dr<h and 0<=c+dc<w and grid[r+dr][c+dc]!="#") :
            continue
        if (s==0 and grid[r+dr][c+dc]=="x") or (s==1 and grid[r+dr][c+dc]=="o") :
            continue
        newDist = dist[r][c][s] +1
        if grid[r+dr][c+dc]== "?" :
            if newDist < dist[r+dr][c+dc][1-s]:
                dist[r+dr][c+dc][1-s] = newDist
                que.append((r+dr,c+dc,1-s))
        else  :
            if newDist < dist[r+dr][c+dc][s] :
                dist[r+dr][c+dc][s] = newDist
                que.append((r+dr,c+dc,s))
print(-1)

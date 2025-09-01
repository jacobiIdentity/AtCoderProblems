#!/usr/bin/env python3
# import sys
from collections import defaultdict,deque

h,w,d = map(int,input().split())
grid = [input() for _ in range(h)]
q = deque()
for i in range(h) :
    for j in range(w) :
        if grid[i][j] == 'H' :
            q.append((i,j,0))
visited = [[-1]*w for _ in range(h)]
ans1 = set()
ans2 = 0
while q :
    x,y,length = q.popleft()
    if visited[x][y] != -1 : continue
    visited[x][y] = length
    if length <= d and grid[x][y] != '#' :
        ans1.add((x,y))
        ans2 += 1
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)] :
        if 0<=x+dx < h and 0<=y+dy<w and grid[x+dx][y+dy] != '#' :
            q.append((x+dx,y+dy,length+1))
    
print(ans2)
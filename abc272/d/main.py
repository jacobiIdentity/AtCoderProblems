#!/usr/bin/env python3
from collections import deque
n,m = (map(int,input().split()))
dir = []
i=0
while i**2<m+1 :
    j = 0
    while i**2+j**2 < m+1 :
        if i**2+j**2 == m :
            dir.append((i,j))
            dir.append((i,-j))
            dir.append((-i,j))
            dir.append((-i,-j))
        j+= 1
    i+=1
# print(dir)
ans = [[-1]*n for _ in range(n) ]
que = deque()
que.append((0,0,0))
while que :
    x,y,stp = que.popleft()
    if ans[x][y] > -1 : continue
    ans[x][y] = stp
    for dx,dy in dir :
        if 0<=x+dx<n and 0<=y+dy<n :
            que.append((x+dx,y+dy,stp+1))
for i in range(n) :
    print(*ans[i])
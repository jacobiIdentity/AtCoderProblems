#!/usr/bin/env python3
from collections import deque
h,w = map(int,input().split())
s_hw = [list(input()) for _ in range(h)]
que = deque()
for i in range(h) :
    for j in range(w) :
        if s_hw[i][j]=="E" :
            que.append((i,j))
while que :
    vx,vy = que.popleft()
    for dx,dy,mark in [(0,1,"<"),(1,0,"^"),(0,-1,">"),(-1,0,"v")] :
        if 0<=vx+dx<h and 0<=vy+dy<w and s_hw[vx+dx][vy+dy]=="." :
            s_hw[vx+dx][vy+dy] = mark
            que.append((vx+dx,vy+dy))
for i in range(h) :
    print("".join(s_hw[i]))
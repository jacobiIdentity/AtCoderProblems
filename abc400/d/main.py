#!/usr/bin/env python3
from collections import deque
h,w = map(int,input().split())
s_h = [input() for _ in range(h)]
a,b,c,d = map(int,input().split())
a,b,c,d = a-1,b-1,c-1,d-1
que = deque()
que.append((a,b,0))
visited = [[0]*w for _ in range(h)]
while que :
    x,y,cnt = que.popleft()
    if visited[x][y] :
        continue
    visited[x][y] = 1
    if x==c and y==d :
        print(cnt)
        exit()
    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)] :
        if 0<=x+dx<h and 0<=y+dy<w :
            if s_h[x+dx][y+dy] == '.' :
                que.appendleft((x+dx,y+dy,cnt))
            else :
                que.append((x+dx,y+dy,cnt+1))
                if 0<=x+2*dx<h and 0<=y+2*dy<w :
                    que.append((x+2*dx,y+2*dy,cnt+1))


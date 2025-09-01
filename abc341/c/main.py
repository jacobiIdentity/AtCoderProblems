#!/usr/bin/env python3
h,w,n = map(int, input().split())
t = input()
grid = [input() for _ in range(h)]
dir = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
ans = 0
moveX,moveY= 0,0
iMin,iMax,jMin,jMax = 1,h-1,1,w-1
for i in range(n) :
    moveX +=dir[t[i]][0]
    moveY +=dir[t[i]][1]
    iMin = max(iMin,1-moveX)
    iMax = min(iMax,h-1-moveX)
    jMin = max(jMin,1-moveY)
    jMax = min(jMax,w-1-moveY)
for i in range(iMin,iMax) :
    for j in range(jMin,jMax) :
        nx,ny = i,j
        if grid[i][j]=='#' :
            continue
        for k in range(n) :
            isOK = True
            if 0<=nx+dir[t[k]][0]<h and 0<=ny+dir[t[k]][1]<w and grid[nx+dir[t[k]][0]][ny+dir[t[k]][1]]=="." :
                nx += dir[t[k]][0]
                ny += dir[t[k]][1]
            else :
                isOK = False
                break
        if isOK :
            ans += 1
print(ans)
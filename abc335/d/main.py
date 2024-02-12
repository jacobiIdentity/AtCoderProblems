#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
grid = dict()
lu = (2,1)
ru = (1,n)
ld = (n,1)
rd = (n,n)
now = (1,1)
dir = 'R'
for i in range(1,n*n) :
    grid[now] = str(i)
    if dir == 'R' :
        if now == ru :
            ru = (ru[0]+1,ru[1]-1)
            dir = 'D'
            now = (now[0]+1,now[1])
        else :
            now = (now[0],now[1]+1)
    elif dir == 'D' :
        if now == rd :
            rd = (rd[0]-1,rd[1]-1)
            dir = 'L'    
            now = (now[0],now[1]-1)
        else :
            now = (now[0]+1,now[1])
    elif dir == 'L' :
        if now == ld :
            ld = (ld[0]-1,ld[1]+1)
            dir = 'U'
            now = (now[0]-1,now[1])
        else :
            now = (now[0],now[1]-1)
    else :
        if now == lu :
            lu = (lu[0]+1,lu[1]+1)
            dir = 'R'
            now = (now[0],now[1]+1)
        else :
            now = (now[0]-1,now[1])
for i in range(1,n+1) :
    row = []
    for j in range(1,n+1) :
        if i == (n+1)//2 and j == (n+1)//2 :
            row.append('T')
        else :
            row.append(grid[(i,j)])
    print(*row)
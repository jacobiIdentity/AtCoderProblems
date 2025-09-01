#!/usr/bin/env python3
w,h,n = map(int,input().split())
grid = [[1]*w for i in range(h) ]
for _ in range(n) :
    x,y,a = map(int,input().split())
    if a==1 :
        for i in range(h) :
            for j in range(x) :
                grid[i][j] = 0
    if a==2 :
        for i in range(h) :
            for j in range(x,w) :
                grid[i][j] = 0
    if a==3 :
        for i in range(y) :
            for j in range(w) :
                grid[i][j] = 0
    if a==4 :
        for i in range(y,h) :
            for j in range(w) :
                grid[i][j] = 0
# print(grid)
print(sum([sum(grid[i]) for i in range(h)]))
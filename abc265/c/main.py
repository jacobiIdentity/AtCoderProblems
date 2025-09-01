#!/usr/bin/env python3
h,w = map(int ,input().split())
grid = [input() for _ in range(h)]
i,j = 0,0
visited = set()
while True :
    if (i,j) in visited :
        print(-1)
        exit()
    visited.add((i,j))
    if grid[i][j] == 'U' and i > 0 :
        i,j = i-1,j
    elif grid[i][j] == 'D' and i < h-1 :
        i,j = i+1,j
    elif grid[i][j] == 'L' and j > 0 :
        i,j = i,j-1
    elif grid[i][j] == 'R' and j < w-1 :
        i,j = i,j+1
    else :
        print(i+1,j+1)
        exit()

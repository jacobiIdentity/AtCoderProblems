#!/usr/bin/env python3
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
for i in range(r) :
    for j in range(c) :
        if grid[i][j] == '.' or grid[i][j] == '#' :
            continue
        b = int(grid[i][j])
        for k in range(r) :
            for l in range(c) :
                if abs(k-i) + abs(l-j) < b+1 and grid[k][l] == '#' :
                    grid[k][l] = '.'
        grid[i][j] = '.'
for i in range(r) :
    print(''.join(grid[i]))

                    
#!/usr/bin/env python3
grid = [input() for _ in range(8)]
row,col = set(), set()
for i in range(8) :
    for j in range(8) :
        if grid[i][j] == '#' :
            row.add(i)
            col.add(j)
print((8-len(row))*(8-len(col)))
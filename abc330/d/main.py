#!/usr/bin/env python3
n = int(input())
grid = [input() for _ in range(n)]
rows = {x:grid[x].count("o") for x in range(n)}
cols = {y:[grid[x][y] for x in range(n)].count("o") for y in range(n)}
# print(rows)
# print(cols)
ans = 0
for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 'o' :
            ans += max(rows[i]-1,0)*max(cols[j]-1,0)
print(ans)
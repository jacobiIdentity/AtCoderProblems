#!/usr/bin/env python3
grid = [input() for _ in range(9)]
# print(grid)
squares = set()
ans = 0
for i in range(9) :
    for j in range(9) :
        for k in range(9) :
                for l in range(9) :
                    if k==0 and l==0 : continue
                    if grid[i][j] == '#' and \
                       0 <= i+k   <= 8 and 0 <= j+l   <= 8 and grid[i+k][j+l] == '#' and \
                       0 <= i+k-l <= 8 and 0 <= j+k+l <= 8 and grid[i+k-l][j+k+l] == '#' and \
                       0 <= i-l   <= 8 and 0 <= j+k   <= 8 and grid[i-l][j+k] == '#' :
                        vertex = tuple(sorted([(i,j),(i+k,j+l),(i+k-l,j+k+l),(i-l,j+k)]))
                        if vertex not in squares :
                            ans += 1
                            squares.add(vertex)

                        # print(i+1,j+1," ", i+k+1,j+l+1," ", i+k-l+1,j+k+l+1," ", i-l+1,j+k+1)
                        # ans += 1
                    # print(i,j,k)
print(ans)
# print(squares)
#!/usr/bin/env python3
h,w,x,y = map(int,input().split())
grid = [input() for _ in range(h)]
t = input()
x -= 1
y -= 1
ans = set()
if grid[x][y] == '@' :
    ans.add((x,y))
for direction in t :
    # print(x,y)
    dx,dy = 0,0
    if direction == 'U' :
        dx,dy = -1,0
    if direction == 'D' :
        dx,dy = 1,0
    if direction == 'L' :
        dx,dy = 0,-1
    if direction == 'R' :
        dx,dy = 0,1
    if 0<=x+dx<h and 0<=y+dy<w and grid[x+dx][y+dy] != '#':
        if grid[x+dx][y+dy] == '@' :
            ans.add((x+dx,y+dy))
        x,y = x+dx,y+dy
print(x+1,y+1,len(ans))
# print(ans)

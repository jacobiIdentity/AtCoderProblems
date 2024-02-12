#!/usr/bin/env python3
h,w,n = map(int, input().split())
grid = [["."]*w for _ in range(h)]
now = (0,0)
direction = "u"
for i in range(n) :
    if grid[now[0]][now[1]] == "." :
        grid[now[0]][now[1]] = "#"
        if direction == "u" :
            direction = "r"
            now = (now[0], (now[1]+1)%w)
        elif direction == "r" :
            direction = "d"
            now = ((now[0]+1)%h, now[1])
        elif direction == "d" :
            direction = "l"
            now = (now[0], (now[1]-1)%w)
        elif direction == "l" :
            direction = "u"
            now = ((now[0]-1)%h, now[1])
    else :
        grid[now[0]][now[1]] = "."
        if direction == "u" :
            direction = "l"
            now = (now[0], (now[1]-1)%w)
        elif direction == "l" :
            direction = "d"
            now = ((now[0]+1)%h, now[1])
        elif direction == "d" :
            direction = "r"
            now = (now[0], (now[1]+1)%w)
        elif direction == "r" :
            direction = "u"
            now = ((now[0]-1)%h, now[1])
for i in range(h) :
        print("".join(grid[i]))

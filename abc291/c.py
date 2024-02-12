#!/usr/bin/env python3
import sys
n = int(input())
s = input()
visited = set()
visited.add((0, 0))
x, y = 0, 0
for i in range(n) :
    if s[i] == 'R' :
        visited.add((x+1,y))
        x += 1
    elif s[i] == 'L' :
        visited.add((x-1,y))
        x -= 1
    elif s[i] == 'U' :
        visited.add((x,y+1))
        y += 1
    else :
        visited.add((x,y-1))
        y -= 1
print('Yes' if len(visited) != n+1 else 'No')
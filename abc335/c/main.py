#!/usr/bin/env python3
from collections import deque
n, q = map(int, input().split())
dragons = [(0,0)]+[(i,0) for i in range(n,0,-1)]
move = 0
for _ in range(1,q+1) :
    x, y = input().split()
    if int(x) == 1 :
        if y == 'R' :
            dragons.append((dragons[-1][0]+1, dragons[-1][1]))
        elif y == 'L' :
            dragons.append((dragons[-1][0]-1, dragons[-1][1]))
        elif y == 'U' :
            dragons.append((dragons[-1][0], dragons[-1][1]+1))
        else :
            dragons.append((dragons[-1][0], dragons[-1][1]-1))
        move += 1
    else :
        print(dragons[-int(y)][0],dragons[-int(y)][1])

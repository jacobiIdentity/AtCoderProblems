#!/usr/bin/env python3
n  = int(input())
dots = [list(map(int,input().split())) for i in range(n)]
for i in range(n) :
    farthest = 1
    distance = 0
    for j in range(n) :
        tmp = (dots[i][0]-dots[j][0])**2 + (dots[i][1]-dots[j][1])**2
        if tmp > distance :
            farthest = j+1
            distance = tmp
    print(farthest)
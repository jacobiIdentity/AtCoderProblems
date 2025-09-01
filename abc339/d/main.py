#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)
def move(p1_x,p1_y,p2_x,p2_y,stepTmp) :
    global step
    if p1_x == p2_x and p2_x == p2_y :
        step = min(step,stepTmp)
    else :
        if p1_x < n-1 and s_n[p1_x+1][p1_y] != '#' :
        move(p1_x+1)
        

n = int(input())
s_n = [input() for _ in range(n)]
p1,p2 = (-1,-1),(-1,-1)
for i in range(n) :
    for j in range(n) :
        if s_n[i][j] == "P" :
            if p1 == (-1,-1) :
                p1 = (i,j)
            else :
                p2 = (i,j)

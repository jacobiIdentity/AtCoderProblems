#!/usr/bin/env python3
import math
n = int(input())
x_y = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]+[[0,0]]
ans = 0
now = (0,0)
for i in range(n+1) :
    ans += math.sqrt((x_y[i+1][0]-x_y[i][0])**2+(x_y[i+1][1]-x_y[i][1])**2)
print(ans)
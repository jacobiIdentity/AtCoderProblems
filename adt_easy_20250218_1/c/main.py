#!/usr/bin/env python3
n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
for i in range(n) :
    ans = 0
    tmp = 0
    for j in range(n) :
        if i == j : continue
        if tmp < (d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2 :
            ans = j
            tmp = (d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2
    print(ans+1)
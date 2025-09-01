#!/usr/bin/env python3
def calcTP(i,j) :
    tmps = 0,0,0,0,0
    for k in range(5) :
        tmps[k] = max(abcdes[i][k],abcdes[j][k])
    return min(tmps)
n = int(input())
abcdes = [list(map(int,input().split())) for _ in range(n)]
tmpScore,tmpI,tmpJ = 0,0,1
for ii in range(n) :
    for jj in range(n) :
        if jj == ii :
            continue
        if tmpScore <
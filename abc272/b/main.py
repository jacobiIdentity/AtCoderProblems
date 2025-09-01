#!/usr/bin/env python3
n,m = map(int,input().split())
oks = [[0]*n for _ in range(n)]
for _ in range(m) :
    ki, *x_ki = map(int,input().split())
    for i in x_ki :
        for j in x_ki :
            if i==j: continue
            oks[i-1][j-1] = 1
            oks[j-1][i-1] = 1
isN = False
for i in range(n) :
    if sum(oks[i]) < n-1 :
        isN = True
print('YNeos'[isN::2])
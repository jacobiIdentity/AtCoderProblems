#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
b_ij = [list(map(int,input().split())) for _ in range(n)]
isYes = True
for i in range(n) :
    if i < n-1 and b_ij[i+1][0] != b_ij[i][0]+7 :
        isYes = False
        break
    for j in range(m-1) :
        if b_ij[i][j+1] != b_ij[i][j]+1 or (b_ij[i][j+1]-1)%7+1 != (b_ij[i][j]-1)%7+1+1 :
            isYes = False
            break
print('YNeos'[not(isYes)::2])
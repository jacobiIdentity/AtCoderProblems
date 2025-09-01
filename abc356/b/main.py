#!/usr/bin/env python3
n,m = map(int,input().split())
a_m = list(map(int,input().split()))
x_ij = [list(map(int,input().split())) for _ in range(n)]
isOKs = [0]*m
for j in range(m) :
    tmp = 0
    for i in range(n) :
        tmp += x_ij[i][j]
    if  tmp >= a_m[j] :
            isOKs[j] = 1
print('Yes' if sum(isOKs)==m else 'No')

#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
k_sij = [list(map(int,input().split())) for _ in range(m)]
k_sij_set = {i:set(k_sij[i][1:]) for i in range(m)}
p_i = list(map(int,input().split()))
ans = 0
for i in range(1<<n) :
    q_i = [0]*m
    for j in range(n) :
        if i&(1<<j):
            for k in k_sij_set :
                if j+1 in k_sij_set[k] :
                    q_i[k] += 1
                    q_i[k] %= 2
    isOK = True
    for i in range(m) :
        if p_i[i] != q_i[i] :
            isOK = False
    if isOK :
        ans += 1
print(ans)
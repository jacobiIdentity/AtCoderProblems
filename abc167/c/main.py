#!/usr/bin/env python3
from collections import defaultdict
n,m,x = map(int,input().split())
books = [list(map(int,input().split())) for _ in range(n)]
ans = float('inf')
for i in range(1,1<<n) :
    skills = [0]*m
    cost = 0
    for j in range(n) :
        if i&(1<<j) :
            cost += books[j][0]
            for k in range(m) :
                skills[k] += books[j][k+1]
    isOK = True
    for j in range(m) :
        if skills[j] < x :
            isOK = False
            break
    if isOK :
        ans = min(cost,ans)
if ans == float('inf') : ans = -1
print(ans)
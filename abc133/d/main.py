#!/usr/bin/env python3
n = int(input())
ds  = list(map(int, input().split()))
ms = [0]*n
al = sum(ds)
for i in range(0, n-1, 2) :
    al -= 2*ds[i]
ms[n-1] = al
for i in range(n-2, -1, -1) :
    ms[i] = 2*ds[i] -ms[i+1]
print(*ms) 

#!/usr/bin/env python3
n, m = map(int,input().split())
x = 0
now = 1
isNo = False
for _ in range(m+1) :
    x += now
    now *= n
    if x > 10**9 :
        isNo = True
print('inf' if isNo else x)
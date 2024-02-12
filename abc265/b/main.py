#!/usr/bin/env python3
n,m,t = map(int ,input().split())
a_n = list(map(int ,input().split()))
x_y = {}
for _ in range(m) :
    x,y = map(int, input().split())
    x_y[x] = y
isOK = True
for i in range(n-1) :
    if t-a_n[i] <= 0 :
        isOK = False
    t -= a_n[i]
    if i+2 in x_y :
        t += x_y[i+2]
print('Yes' if isOK else 'No')
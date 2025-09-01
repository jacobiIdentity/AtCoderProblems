#!/usr/bin/env python3
n,m,t = map(int ,input().split())
a_n = list(map(int ,input().split()))
x_y = [tuple(map(int,input().split())) for _ in range(m)]
b = 0
isYes = True
for i in range(n-1) :
    if b < m and i+1 == x_y[b][0] :
        t += x_y[b][1]
        b += 1
    t -= a_n[i]
    # print(i,t)
    if  t < 1 :
        isYes = False
print('Yes' if isYes else 'No')
#!/usr/bin/env python3
n = int(input())
t = 1
ans = 1
while t*t*t < n+1 :
    k = str(t*t*t)
    isY = True
    for i in range(len(k)//2) :
        if k[i] != k[len(k)-1-i] : isY = False
    if isY : ans = t*t*t
    t += 1
print(ans)
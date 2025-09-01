#!/usr/bin/env python3
n = int(input())
ans = -1
x = 0
tmp = 0
while tmp <= n :
    if tmp==n :
        ans = x 
        break
    x += 1
    tmp = int(1.08*x)
print(ans if ans>-1 else ':(')
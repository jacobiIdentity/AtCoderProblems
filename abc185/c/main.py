#!/usr/bin/env python3
l = int(input())
r = min(11,l-12)
ans = 1
for i in range(r) :
    ans *= l-i-1
for i in range(r) :
    ans //= (i+1)
print(ans)
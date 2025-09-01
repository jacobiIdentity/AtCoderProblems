#!/usr/bin/env python3
a,b,x = map(int,input().split())
ans = 0
order = 1
for i in range(10) :
    order = 10**i
    if a*order+ b*(i+1) <= x <= a*(order*10-1) + b*(i+1) :
        ans = max(ans,(x-b*(i+1))//a)
    elif a*(order*10-1) + b*(i+1) < x < a*(order*10) + b*(i+2) :
        ans = order*10-1

if x >= a*1000000000+b*10 : ans = 1000000000
print(ans)

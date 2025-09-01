#!/usr/bin/env python3
n = int(input())
ans,tmp = 0,1
while tmp <= n :
    ans += 1
    tmp *= 2
print(ans-1)
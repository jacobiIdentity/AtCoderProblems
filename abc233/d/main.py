#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
l,r = 0,0
tmp = 0
ans = 0
while l<n and r<n :
    tmp += a_n[r]
    if tmp == k : ans += 1
    if tmp >= k :
        tmp -= a_n[l]
        l += 1
        if l > r :
            r += 1
        else :
            tmp -= a_n[r]
    else :
        r += 1
print(ans)

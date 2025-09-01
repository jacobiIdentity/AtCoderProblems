#!/usr/bin/env python3
n,k = map(int, input().split())
a_n = set(map(int,input().split()))
ans = (k*(k+1))//2
for a in a_n :
    if a <= k :
        ans -= a
print(ans)
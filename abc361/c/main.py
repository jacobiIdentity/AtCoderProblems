#!/usr/bin/env python3

n,k = map(int ,input().split())
a_n = sorted(list(map(int ,input().split())))
ans = float('inf')
for i in range(k+1) :
    ans = min(ans, a_n[n-1-i]-a_n[k-i])
print(ans)

#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
x_n = [0]+list(map(int,input().split()))
d = defaultdict(int)
for _ in range(m) :
    c,y = map(int,input().split())
    d[c] = y
dp =[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1) :
    for j in range(n+1) :
        dp[i][0] = max(dp[i][0],dp[i-1][j])
        if j > 0 and i >= j:
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+x_n[i]+d[j])
print(max(dp[n]))
# print(dp)
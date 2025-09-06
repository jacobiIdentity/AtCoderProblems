#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
acs =  list(itertools.accumulate([0]+a_n))
dp = [[float('inf')]*(n+1) for _ in range(n)]
for k in range(1,n+1) :
    for i in range(n) :
        if i+k > n :
            break
        if k== 1 :
            dp[i][i+k] = 0
            continue
        for l in range(1,k) :
            dp[i][i+k] = min(dp[i][i+k],dp[i][i+l]+dp[i+l][i+k]+acs[i+k]-acs[i])
print(dp[0][-1])
# print(dp)


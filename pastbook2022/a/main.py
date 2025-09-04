#!/usr/bin/env python3
n = int(input())
c_ij = [list(map(int,input().split())) for _ in range(n+1)]
dp = [float("inf")]*(n+1)
dp[0]=0
for i in range(1,n+1) :
    for j in range(i) :
        dp[i] = min(dp[j]+c_ij[i][j],dp[i])
print(dp[-1])
# print(dp)
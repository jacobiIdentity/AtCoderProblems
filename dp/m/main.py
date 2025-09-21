#!/usr/bin/env python3
n,k = map(int,input().split())
# a_n = [0]+ list(map(int,input().split()))
# acs = [0]*(n+1)
# for i in range(n) :
#     acs[i+1] += acs[i]+a_n[i]
a_n = list(map(int,input().split()))
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n) :
    for j in range(k) :
        l = 1
        while l <= a_n[i] and l+j<=k :
            print(i,j,l,dp[i][j])
            dp[i+1][j+l] += dp[i][j]
            l += 1
print(dp[-1][-1])
print(dp)
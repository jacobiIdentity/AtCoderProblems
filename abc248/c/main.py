#!/usr/bin/env python3
n,m,k = map(int,input().split())
dp = [[0]*(n*m+1) for _ in range(n+1)]
for i in range(1,m+1) :
    dp[1][i] = 1
for i in range(2,n+1) :
    for p in range(i-1,m*(i-1)+1) :
        for q in range(1,m+1) :
            dp[i][p+q] += dp[i-1][p]*dp[1][q]
            dp[i][p+q] %= 998244353
print(sum(dp[n][n:k+1])%998244353)
# print(dp)
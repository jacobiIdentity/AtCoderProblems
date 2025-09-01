#!/usr/bin/env python3
n,x,y = map(int,input().split())
q = []
dp = [[0]*n for _ in range(2)]
dp[0][n-1] = 1
for i in reversed(range(1,n)) :
    dp[1][i] += x*dp[0][i]
    dp[0][i-1] += dp[0][i]
    dp[0][i-1] += dp[1][i]
    dp[1][i-1] += y*dp[1][i]
print(dp[1][0])
# print(dp)
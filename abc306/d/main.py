#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
x_y = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(2) for _ in range(n+1)]
for i in range(n+1) :
    if i == 0 :
        continue
    if x_y[i-1][0] == 0 :
        dp[i][0] = max(dp[i-1][0],dp[i-1][0]+x_y[i-1][1],dp[i-1][1]+x_y[i-1][1])
        dp[i][1] = dp[i-1][1]
    else :
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]+x_y[i-1][1])
print(max(dp[n][0],dp[n][1]))

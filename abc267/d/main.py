#!/usr/bin/env python3
n,m = map(int,input().split())
a_n =list( map(int,input().split()))
dp = [[-float('inf')]*(m+1) for _ in range(n+1)]
for i in range(n+1) :
    for j in range(m+1) :
        if j==0 :
            dp[i][0] = 0
            continue
        if j>i:
            break
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+j* a_n[i-1])
# print(dp)
print(dp[n][m])
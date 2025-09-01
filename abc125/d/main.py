#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
dp = [[0]*2 for _ in range(n)]
dp[1][0] = a_n[0]+a_n[1]
dp[1][1] = -dp[1][0]
for i in range(2,n) :
    dp[i][0] = max(dp[i-1])+a_n[i]
    dp[i][1] = max(dp[i-1][0]-2*a_n[i-1],dp[i-1][1]+2*a_n[i-1])-a_n[i]
print(max(dp[-1]))
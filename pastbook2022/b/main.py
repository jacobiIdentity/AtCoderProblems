#!/usr/bin/env python3
m,n = map(int,input().split())
s= '.'+input()
t= '.'+input()
dp = [[float('inf')]*(n+1) for _ in range(m+1)]
for i in range(m+1) :
    for j in range(n+1):
        if j==0 :
            dp[i][j] = i
        elif i==0 :
            dp[i][j]=j
        elif s[i]==t[j]:
            dp[i][j] = dp[i-1][j-1]
        else :
            dp[i][j] = min(dp[i-1][j-1]+1,dp[i][j-1]+1,dp[i-1][j]+1)
print(dp[-1][-1])
# print(dp)
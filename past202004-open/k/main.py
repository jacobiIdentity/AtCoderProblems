#!/usr/bin/env python3
n = int(input())
s = "0"+input()
c_n = [0]+list(map(int,input().split()))
d_n = [0]+list(map(int,input().split()))
dp = [[float("inf")]*(n+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1) :
    for j in range(n+1) :
        dp[i][j] = min(dp[i][j],dp[i-1][j]+d_n[i])
        if j>0 :
            dp[i][j] = min(dp[i][j],dp[i-1][j-1]+(0 if s[i]=="(" else c_n[i])) 
        if j<n :
            dp[i][j] = min(dp[i][j],dp[i-1][j+1]+(0 if s[i]==")" else c_n[i])) 
print(dp[-1][0])
# print(dp)
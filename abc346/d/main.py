#!/usr/bin/env python3
n = int(input())
s = input()
c_n = list(map(int,input().split()))
dp = [[float('inf')]*4 for _ in range(n)]
if s[0] == '0' :
    dp[0][2] = 0
    dp[0][3] = c_n[0]
else :
    dp[0][2] = c_n[0]
    dp[0][3] = 0
for i in range(1,n) :
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = min(dp[i-1][0],dp[i-1][3])
    dp[i][2] = dp[i-1][3]
    dp[i][3] = dp[i-1][2]
    if s[i] == '0' :
        dp[i][1] +=  c_n[i]
        dp[i][3] +=  c_n[i]
    else :
        dp[i][0] +=  c_n[i]
        dp[i][2] +=  c_n[i]
print(min(dp[n-1][0],dp[n-1][1]))
# print(dp)
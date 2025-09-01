#!/usr/bin/env python3
n = int(input())
s = input()
dp = [[0]*2 for _ in range(n+1)]
for i in range(1,n+1) :
    if s[i-1]=="0" :
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][0]+1
    else :
        dp[i][0] = dp[i-1][0]+1
        dp[i][1] = dp[i-1][1]
print(sum([dp[i][0] for i in range(n+1)]))
# print(dp)
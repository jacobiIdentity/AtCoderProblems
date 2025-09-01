#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    n = int(input())
    s = input()
    dp = [[float('inf')]*3 for _ in range(n+1)]
    for i in range(n+1) :
        if i == 0 :
            dp[i][0] = 0
            continue
        dp[i][0] = dp[i-1][0]+int(s[i-1])
        dp[i][1] = min(dp[i-1][0],dp[i-1][1])+1-int(s[i-1])
        dp[i][2] = min(dp[i-1][1],dp[i-1][2])+int(s[i-1])
    print(min(dp[n]))
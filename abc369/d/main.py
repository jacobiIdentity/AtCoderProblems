#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
dp = [[-1]*4 for _ in range(n+1)]
for i in range(1,n+1) :
    if i == 1 :
        dp[i][0] = a_n[0]
        dp[i][1] = 0
    else :
        # Odd and Yes
        if dp[i-1][2] != -1 :
            dp[i][0] = max(dp[i][0],dp[i-1][2]+a_n[i-1])
        if dp[i-1][1] != -1 :
            dp[i][0] = max(dp[i][0],dp[i-1][1]+a_n[i-1])
        # Odd and No
        if dp[i-1][1] != -1 :
            dp[i][1] = max(dp[i][1],dp[i-1][1])
        if dp[i-1][2] != -1 :
            dp[i][1] = max(dp[i][1],dp[i-1][2])
        # Even and Yes
        if dp[i-1][0] != -1 :
            dp[i][2] = max(dp[i][2],dp[i-1][0]+a_n[i-1]*2)
        if dp[i-1][3] != -1 :
            dp[i][2] = max(dp[i][2],dp[i-1][3]+a_n[i-1]*2)
        # Even and No
        if dp[i-1][0] != -1 :
            dp[i][3] = max(dp[i][3],dp[i-1][0])
        if dp[i-1][3] != -1 :
            dp[i][3] = max(dp[i][3],dp[i-1][3])
print(max(dp[n]))
# print(*dp)
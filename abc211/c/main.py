#!/usr/bin/env python3
s = '0'+input()
c = '0chokudai'
dp = [[1]*len(s)]+[[0]*(len(s)) for _ in range(len(c)-1)]
for i in range(1,len(c)) :
    for j in range(1,len(s)) :
        if s[j] != c[i] :
            dp[i][j] = dp[i][j-1]
        else :
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
print(dp[len(c)-1][len(s)-1]%((10**9+7)))

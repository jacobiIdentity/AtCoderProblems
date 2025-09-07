#!/usr/bin/env python3
s = input()
n = len(s)
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(3,n+1) :
    for l in range(n+1) :
        if i+l>n :
            break
        r = l+i
        if i==3 and s[l:r]=="iwi" :
            dp[l][r] = 1
            continue
        for m in range(l,r) :
            dp[l][r] = max(dp[l][r],dp[l][m]+dp[m][r])
        if s[l]=="i" and s[r-1]=="i" :
            for m in range(l+1,r-1) :
                if s[m] == "w" and m-l-1==3*dp[l+1][m] and r-m-2 ==3*dp[m+1][r-1] :
                    dp[l][r] = max(dp[l][r],dp[l+1][m]+dp[m+1][r-1]+1)
print(dp[0][n])
# print(dp)

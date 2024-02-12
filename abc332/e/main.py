#!/usr/bin/env python3
def sumsquared(fukuro) :
    return sum([f**2 for f in fukuro])
n,d = map(int ,input().split())
w_n = sorted(list(map(int ,input().split())), reverse=True) 
dp = [[0]*d for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(d) :
        dp[i][j] = dp[i-1][j]
    tmpJ = 0
    tmpSS = 10**9
    for j in range(d) :
        dp[i][j] += w_n[i-1]
        nowSS = sumsquared(dp[i])
        # print(tmpSS, nowSS)
        if tmpSS > nowSS :
            tmpSS, tmpJ = nowSS, j
        dp[i][j] -= w_n[i-1]
    dp[i][tmpJ] += w_n[i-1]
# print(dp)
print('{:.20f}'.format(sumsquared(dp[n])/d-(sum(w_n)/d)**2))
        

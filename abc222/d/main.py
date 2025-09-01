#!/usr/bin/env python3
n = int(input())
a_n = [0]+list(map(int,input().split()))
b_n = [0]+list(map(int,input().split()))
# dp = [[0]*(b_n[i]+1) for i in range(n+1)]
dp = [[0]*(3000+1) for i in range(n+1)]
for i in range(1,n+1) :
    for j in range(a_n[i],b_n[i]+1) :
        if i == 1 :
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i-1][j]
    for j in range(a_n[i]+1,3000+1) :
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= 998244353

        # for k in range(a_n[i-1],min(b_n[i-1],j) +1) :
        #     dp[i][j] += dp[i-1][k]
        #     dp[i][j] %= 998244353
# print(sum(dp[n])%998244353)
print(dp[n][b_n[n]]%998244353)
# print(sum(dp[n][a_n[n]:b_n[n]])%998244353)
# print(dp)
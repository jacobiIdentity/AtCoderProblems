#!/usr/bin/env python3
MOD = 10**9 + 7
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n) :
    # 累積和
    acs = [0]*(k+2)
    for j in range(k+1) :
        acs[j+1] = (acs[j]+dp[i][j])%MOD
    
    for j in range(k+1) :
        dp[i+1][j] = acs[j+1]-acs[j-min(a_n[i],j)]
        # l = 0
        # while l <= a_n[i] and l+j<=k :
        #     dp[i+1][j+l] += dp[i][j]
        #     dp[i+1][j+l] %= MOD
        #     l += 1
print(dp[-1][-1]%MOD)
# print(dp)



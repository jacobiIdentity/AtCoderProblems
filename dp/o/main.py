#!/usr/bin/env python3
n = int(input())
a_ij = [list(map(int,input().split())) for _ in range(n)]
MOD = 10**9+7
dp = [0]*(1<<n)
dp[0] = 1
for S in range((1<<n)-1) :
    if dp[S]==0 :
        continue
    k = bin(S).count("1")
    for i in range(n) :
        if S&(1<<i) or a_ij[k][i]==0 :
            continue
        dp[S|(1<<i)] += dp[S]
        dp[S|(1<<i)] %= MOD
print(dp[-1])

# for i in range(n):         # 列（仕事）
#     if (S >> i) & 1:
#         continue           # すでに使っている列はスキップ
#     if a_ij[bin(S).count("1")][i] == 0:
#         continue           # マッチできない
#     dp[S | (1 << i)] = (dp[S | (1 << i)] + dp[S]) % MOD


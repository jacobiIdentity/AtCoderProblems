#!/usr/bin/env python3
n = int(input())
cards = []
for _ in range(n) :
    cards.append(list(map(int, input().split())))
dp = [[1]+[0]*(n-1) for _ in range(2)]
for i in range(1,n) :
    if cards[i][0] != cards[i-1][0] :
        dp[0][i] += dp[0][i-1]
    if cards[i][0] != cards[i-1][1] :
        dp[0][i] += dp[1][i-1]
    if cards[i][1] != cards[i-1][0] :
        dp[1][i] += dp[0][i-1]
    if cards[i][1] != cards[i-1][1] :
        dp[1][i] += dp[1][i-1]
    dp[0][i] %= 998244353
    dp[1][i] %= 998244353
print((dp[0][n-1]+dp[1][n-1])%998244353)

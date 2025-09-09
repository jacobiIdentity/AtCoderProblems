#!/usr/bin/env python3
MOD = 1234567
n,p = map(int,input().split())
h_n = [0]+[int(input()) for _ in range(n)] +[0]
for i in range(n+1) :
    h_n[i+1] += h_n[i]
# print(h_n)
dp = [0]*(n+1)
dp[0] = 1
for i in range(n) :
    for j in range(i+1,n+1) :
        if h_n[j]-h_n[i] <= p:
            dp[j] += dp[i]
            dp[j] %= MOD
        else :
            break
for i in range(n) :
    dp[i+1] += dp[i]
print(dp[-1])


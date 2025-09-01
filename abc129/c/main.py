#!/usr/bin/env python3
import itertools
n,m = map(int,input().split())
a_m = {int(input()) for _ in range(m)}
dp = [0]*(n+1)
if 1 not in a_m :
    dp[1] = 1
if n>1 and 2 not in a_m :
    dp[2] = dp[1]+1
for i in range(3,n+1) :
    if i not in a_m :
        dp[i] = dp[i-1]+dp[i-2]
        dp[i] %= 1000000007
print(dp[n])
# print(dp)
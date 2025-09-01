#!/usr/bin/env python3
n = int(input())
s = "0"+input()
d = {c:i+1 for i,c in enumerate("atcoder")}
# print(d)
dp = [[1]+[0]*7 for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(1,8) :
        dp[i][j] = dp[i-1][j]
        # print(j,s[i],s[i] in d)
        if s[i] in d and d[s[i]]==j:
            dp[i][j] += dp[i-1][j-1]
print(dp[-1][-1]%(10**9+7))
# print(dp)
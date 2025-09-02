#!/usr/bin/env python3
n = int(input())
s = "0"+input()
d = {"J":1,"O":2,"I":4}
dp = [[0]*8 for _ in range(n+1)]
for i in range(1,n+1) :    
    for j in range(8) :
        if d[s[i]]&j == 0:
            continue
        if i == 1 :
            if j&1 :
                dp[i][j] = 1
            continue
        for k in range(8) :
            if k&j :
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= 10007
print(sum(dp[-1])%10007)
# print(dp)
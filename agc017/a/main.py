#!/usr/bin/env python3
n,p= map(int,input().split())
a_n= list(map(int,input().split()))
dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1) :
    if a_n[i-1]%2==0 :
        dp[i][0] = dp[i-1][0]*2
        dp[i][1] = dp[i-1][1]*2
    else :
        dp[i][0] = dp[i-1][0]+dp[i-1][1]
        dp[i][1] = dp[i-1][0]+dp[i-1][1]
print(dp[n][p])
# print(dp)
# どこかで奇数が一回でもあれば dp[i][0]==dp[i][1]=2**(i-1)
# 奇数がなければ dp[i][0]== 2**i, dp[i][1]==0
# となる
# https://img.atcoder.jp/agc017/editorial.pdf
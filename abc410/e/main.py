#!/usr/bin/env python3
n,h,m = map(int,input().split())
dp = [[-1]*(h+1) for _ in range(n+1)]
dp[0][h] = m
for i in range(1,n+1) :
    a,b = map(int,input().split())
    isNG = True
    for j in range(h+1) :
        if j+a<h+1 :
            dp[i][j] = max(dp[i][j],dp[i-1][j+a])
        if dp[i-1][j]>=b :
            dp[i][j] = max(dp[i][j],dp[i-1][j]-b)
        if dp[i][j]>-1 :
            isNG = False
    if isNG :
        print(i-1)
        exit()
print(n)
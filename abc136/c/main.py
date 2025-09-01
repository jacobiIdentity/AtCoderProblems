#!/usr/bin/env python3
n = int(input())
h_n = [0]+ list(map(int,input().split()))
dp = [[True,True] for _ in range(n+1)]
for i in range(1,n+1) :
    if not((dp[i-1][0] and h_n[i-1]<=h_n[i]) or  (dp[i-1][1] and h_n[i-1]-1<=h_n[i])) :
        dp[i][0] = False
    if not((dp[i-1][0] and h_n[i-1]<=h_n[i]-1) or  (dp[i-1][1] and h_n[i-1]-1<=h_n[i]-1)) :
        dp[i][1] = False
print('YNeos'[not(dp[n][0] or dp[n][1])::2])
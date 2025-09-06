#!/usr/bin/env python3
n,w = map(int,input().split())
w_v = [list(map(int,input().split())) for _ in range(n)]
dp =  [[0]*(w+1) for _ in range(n+1)]
# print(w_v)
for i in range(1,n+1) :
    w_i,v_i = w_v[i-1][0],w_v[i-1][1]
    if i == 1 :
        dp[i][w_i] = v_i
        continue
    for j in range(w+1) :        
        dp[i][j] = max(dp[i][j],dp[i-1][j])
        if j+w_i<= w :
            dp[i][j+w_i] = max(dp[i-1][j]+v_i,dp[i-1][j+w_i])
print(max(dp[-1]))
# print(dp)
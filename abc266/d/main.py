#!/usr/bin/env python3
n = int(input())
t_x_a = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*(5) for _ in range(t_x_a[-1][0]+1)]
now = 0
for i in range(t_x_a[-1][0]+1) :
    if i==0 :
        dp[i][0] = 0
        continue
    isSnuke = False
    if i==t_x_a[now][0] :
        isSnuke = True
        now += 1
    for j in range(5) :
        if 0 <= j-1 < 5 and dp[i-1][j-1]>= 0 :
            if isSnuke and t_x_a[now-1][1]==j:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+t_x_a[now-1][2])
            else :
                dp[i][j] = max(dp[i][j],dp[i-1][j-1])
        if 0 <= j+1 < 5 and dp[i-1][j+1]>= 0 :
            if isSnuke and t_x_a[now-1][1]==j:
                dp[i][j] = max(dp[i][j],dp[i-1][j+1]+t_x_a[now-1][2])
            else :
                dp[i][j] = max(dp[i][j],dp[i-1][j+1])
        if dp[i-1][j]>= 0 :
            if isSnuke and t_x_a[now-1][1]==j:
                dp[i][j] = max(dp[i][j],dp[i-1][j]+t_x_a[now-1][2])
            else :
                dp[i][j] = max(dp[i][j],dp[i-1][j])
print(max(dp[t_x_a[-1][0]]))
            
# print(dp)
#!/usr/bin/env python3
n,m,k = map(int,input().split())
a_i = [int(input()) for _ in range(n)]
dp = [float("inf")]*(n+1)
dp[0]=0
for i in range(1,n+1) :
    a,b = 0,float("inf")
    for j in range(m) :
        if i-1-j < 0 :
            break
        a = max(a_i[i-1-j],a)
        b = min(a_i[i-1-j],b)
        dp[i] = min(dp[i],dp[i-1-j]+k + (j+1)*(a-b))
print(dp[-1])
# print(dp)


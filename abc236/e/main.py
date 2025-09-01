#!/usr/bin/env python3
def check_ave(x) :
    dp = [[0]*2 for _ in range(n+1)]
    for i in range(1,n+1) :
        dp[i][0] = max(dp[i-1][0],dp[i-1][1])+a_n[i-1]-x
        dp[i][1] = dp[i-1][0]
    return max(dp[-1][0],dp[-1][1])>=0
def check_median(x) :
    dp = [[0]*2 for _ in range(n+1)]
    for i in range(1,n+1) :
        dp[i][0] = max(dp[i-1][0],dp[i-1][1])+ (1 if a_n[i-1]>=x else -1)
        dp[i][1] = dp[i-1][0]
    return max(dp[-1][0],dp[-1][1])>0

n = int(input())
a_n = list(map(int,input().split()))
ok,ng = 0,10**10
for _ in range(100) :
    mid = (ok+ng)/2
    if check_ave(mid) :
        ok = mid
    else :
        ng = mid
print(ok)

ok,ng = 0,10**10
while ng-ok > 1: 
    mid = (ok+ng)//2
    if check_median(mid) :
        ok = mid
    else :
        ng = mid
print(ok)

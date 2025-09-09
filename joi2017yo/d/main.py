#!/usr/bin/env python3
from collections import defaultdict
INF = float('inf')
n,m = map(int,input().split())
toys = [int(input())-1 for _ in range(n)]
d1 = defaultdict(int)
d2 = defaultdict(int)
for i in range(n) :
    d1[toys[i]] += 1
d2[0] = 0
for S in range(1<<m) :
    if S not in d2 :
        continue
    for i in range(m) :
        if S&(1<<i) : continue
        d2[S|(1<<i)] = d2[S]+d1[i]
# print(d1)
# print(d2)
# acs[i][j] =  j-1番目までに おもちゃi が何個あるか
acs = [[0]*(n+1) for _ in range(m) ]
for i in range(n) :
    for j in range(m) :
        acs[j][i+1] += acs[j][i] + (1 if j==toys[i] else 0)
# print(acs)
dp = [INF]*(1<<m)
dp[0] = 0
for S in range((1<<m)-1) :
    if dp[S]== INF : continue
    for j in range(m) :
        if S&(1<<j) : continue
        # 累積和でO(1)で実装可能
        # tmp = 0
        # for k in range(d2[S],d2[S]+d1[j]) :
        #     if toys[k] != j :
        #         tmp+=1
        # dp[S|(1<<j)] = min(dp[S|(1<<j)],dp[S]+tmp)
        # 誤っておいている数
        dp[S|(1<<j)] = min(dp[S|(1<<j)],dp[S]+d1[j]-(acs[j][d2[S]+d1[j]]-acs[j][d2[S]]))
print(dp[-1])
# print(dp)
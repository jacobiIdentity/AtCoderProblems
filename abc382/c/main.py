#!/usr/bin/env python3
import bisect
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
b_m = list(map(int,input().split()))
judgeA = []
now = float('inf')
for i in range(n) :
    if now > a_n[i] :
        judgeA.append(-a_n[i])
        now = a_n[i]
    else :
        judgeA.append(-now)
for i in range(m) :
    ans = bisect.bisect_left(judgeA,-b_m[i])+1
    if ans > n :
        ans = -1
    print(ans)
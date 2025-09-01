#!/usr/bin/env python3
import bisect
n,m= map(int,input().split())
a_n = list(map(int,input().split()))
b_m = list(map(int,input().split()))
acMin = []
tmp = a_n[0]
for i in range(n) :
    tmp = min(tmp,a_n[i])
    acMin.append(-tmp)
for j in range(m) :
    pos = bisect.bisect_left(acMin,-b_m[j])
    if pos == n :
        pos = -2
    pos += 1
    print(pos)


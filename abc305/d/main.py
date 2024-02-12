#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int, input().split()))
sa_n = set(a_n)
q = int(input())
l_r = [list(map(int, input().split())) for _ in range(q)]
sl_r = set(sum(l_r, []))
d1 = defaultdict(int)
for i in range(n) :
    if i%2 != 0 :
        d1[a_n[i]] = d1[a_n[i-1]]
    else :
        d1[a_n[i]] = d1[a_n[i-1]] + a_n[i]-a_n[i-1]
all = sorted(list(sa_n|sl_r))
d2 = defaultdict(int)
t = 0
isAwake = False
for i in all :
    if i in sa_n :
        isAwake = not(isAwake)
        t = i
        d2[i] = d1[i]
        continue
    if isAwake :
        d2[i] = d2[t]
    else :
        d2[i] = d2[t] + i - t
for i in range(q) :
    print(d2[l_r[i][1]]-d2[l_r[i][0]])

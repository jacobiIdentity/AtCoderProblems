#!/usr/bin/env python3
from collections import defaultdict
import sys
n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_m = list(map(int, input().split()))
da = defaultdict(int)
db = defaultdict(int)
for i in range(n) :
    da[a_n[i]] += 1
for i in range(m) :
    db[b_m[i]] += 1
ab = sorted(list(set(list(da) +list(db))))
mb = max(db)
a,b = 0,m
for t in ab :
    a += da[t]
    b -= db[t]
    if t == mb :
        print(t+1)
        exit()
    if a >= b :
        print(t)
        exit()

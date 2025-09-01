#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
q = int(input())
d = defaultdict(int)
for a in a_n :
    d[a] += 1
s = sum(a_n)
for _ in range(q) :
    b,c = map(int,input().split())
    if b in d :
        s -= b*d[b]
        s += c*d[b]
        d[c] += d[b]
        d[b] = 0
    print(s)

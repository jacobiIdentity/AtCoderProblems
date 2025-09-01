#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
p_n = list(map(int,input().split()))
p2  = defaultdict(int)
for p in p_n :
    p2[p] += 1
ranks = defaultdict(int)
r = 1
for p in reversed(sorted(p2)) :
    ranks[p] = r
    r += p2[p]
for p in p_n :
    print(ranks[p])
#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
d = defaultdict(set)
for _ in range(n-1) :
    a,b = map(int,input().split())
    d[a].add(b)
    d[b].add(a)
isYes = False
for dd in d :
    if len(d[dd]) == n-1 : isYes = True
print('YNeos'[not(isYes or n==1)::2])
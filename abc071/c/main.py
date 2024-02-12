#!/usr/bin/env python3
import sys
from collections import defaultdict
n = int(input())
a_n  = list(map(int, input().split()))
d = defaultdict(int)
for a in a_n :
    d[a] += 1
p, q = 0, 0
for dd in d :
    if d[dd] < 2 :
        continue
    if q < dd :
        if d[dd] > 3 :
            p, q = dd, dd
        else :
            p, q = q, dd
    elif p < dd :
        p = dd
print(p*q)
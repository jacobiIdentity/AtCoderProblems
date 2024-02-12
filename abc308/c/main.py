#!/usr/bin/env python3
from functools import cmp_to_key
def cmp(x,y) :
    if x[1]*y[2] < x[2]*y[1] :
        return 1
    elif x[1]*y[2] > x[2]*y[1] :
        return -1
    elif x[0] > y[0]:
        return 1
    elif x[0] < y[0]:
        return -1
    else :
        return 0
n = int(input())
l = list()
for i in range(n) :
    a, b = map(int, input().split())
    l.append((i+1, a, a+b))
print(*[t[0] for t in sorted(l, key=cmp_to_key(cmp))])
#!/usr/bin/env python3
import bisect
n,q = map(int,input().split())
tmp = list(map(int,input().split()))
a_n = [-a for a in tmp]
a_n.sort()
for _ in range(q) :
    print(bisect.bisect_right(a_n,-int(input())))
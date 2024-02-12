#!/usr/bin/env python3
import bisect
h, w, n = map(int, input().split())
aSet = set()
bSet = set()
a_b = []
for i in range(n) :
    a, b = map(int, input().split())
    aSet.add(a)
    bSet.add(b)
    a_b.append((a,b))
hList = sorted(list(aSet))
wList = sorted(list(bSet))
for i in range(n) :
    print(bisect.bisect(hList,a_b[i][0]),bisect.bisect(wList,a_b[i][1]))
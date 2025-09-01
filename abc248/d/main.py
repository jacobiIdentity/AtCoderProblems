#!/usr/bin/env python3
from collections import defaultdict
import bisect
n = int(input())
a_n = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n) :
    d[a_n[i]].append(i+1)
for k in d :
    d[k].sort()
q = int(input())
for _ in range(q) :
    l,r,x = map(int,input().split())
    if len(d[x]) == 0 :
        print(0)
        continue
    lPos = bisect.bisect_left(d[x],l)
    rPos = bisect.bisect_right(d[x],r)
    print(rPos-lPos)
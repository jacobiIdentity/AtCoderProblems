#!/usr/bin/env python3
import bisect
l,q = map(int,input().split())
a = [0,l]
for _ in range(q) :
    c,x = map(int,input().split())
    if c == 1 :
        a.append(x)
        a.sort()
    else :
        pos = bisect.bisect(a,x)
        print(a[pos]-a[pos-1])
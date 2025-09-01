#!/usr/bin/env python3
import bisect
n,m = map(int,input().split())
a_m = list(map(int,input().split()))
for i in range(1,n+1) :
    pos = bisect.bisect_left(a_m,i)
    print(a_m[pos]-i)
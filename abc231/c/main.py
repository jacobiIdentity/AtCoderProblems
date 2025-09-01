#!/usr/bin/env python3
import bisect
n,q = map(int,input().split())
a_n = sorted(list(map(lambda x:-int(x),input().split())))
for _ in range(q) :
    x = -int(input())
    print(bisect.bisect_right(a_n,x))

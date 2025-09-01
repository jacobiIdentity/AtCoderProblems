#!/usr/bin/env python3
import bisect
n = int(input())
a_n = list(map(int,input().split()))
ans = 0
a_n.sort()
ok,ng = 0,max(a_n)
while ng-ok>1 :
    mid = (ok+ng)//2
    pos = bisect.bisect_left(a_n,mid)
    if n-pos >= mid :
        ok = mid
    else :
        ng = mid
print(ok)
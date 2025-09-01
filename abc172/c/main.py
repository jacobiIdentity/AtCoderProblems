#!/usr/bin/env python3
import itertools,heapq
from collections import defaultdict
n,m,k = map(int,input().split())
a_n = [0]+list(map(int,input().split()))
b_m = [0]+list(map(int,input().split()))
acsA = list(itertools.accumulate(a_n))
acsB = list(itertools.accumulate(b_m))
ans = 0
for i in range(m+1) :
    if acsB[i] > k :
        break
    ok,ng = 0,n+1
    while ng-ok > 1 :
        mid = (ok+ng)//2
        if acsB[i]+acsA[mid]<= k :
            ok = mid
        else :
            ng = mid
    ans = max(ok+i,ans)
print(ans)
#!/usr/bin/env python3
import bisect
n,m = map(int,input().split())
a_n = set(map(int,input().split()))
b_m = set(map(int,input().split()))
aList = sorted(list(a_n))
bList = sorted(list(b_m))
ans = float('inf')
for a in a_n :
    if a in b_m :
        ans = 0
        break
    pos = bisect.bisect_left(bList,a)
    if 0 <= pos < len(bList) :
        ans = min(ans,abs(bList[pos]-a))
    if pos < len(bList)-1:
        ans = min(ans,abs(bList[pos+1]-a))
    if pos > 0:
        ans = min(ans,abs(bList[pos-1]-a))
print(ans)
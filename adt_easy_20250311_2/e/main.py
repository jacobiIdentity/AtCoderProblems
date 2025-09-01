#!/usr/bin/env python3
import bisect
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
a_n.sort()
ans = 0
for i in range(n) :
    pos = bisect.bisect_left(a_n,a_n[i]+m)
    ans = max(ans,pos-i)
print(ans)
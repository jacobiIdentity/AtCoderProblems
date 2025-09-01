#!/usr/bin/env python3
from collections import defaultdict
n,c = map(int,input().split())
d = defaultdict(int)
for _ in range(n) :
    a,b,c_ = map(int,input().split())
    d[a] += c_
    d[b+1] -= c_
# print(d)
ans = 0
nowCost = 0
nowDay = 1
for i in sorted(d) :
    # print(nowDay,nowCost,i,d[i],ans,min(c,nowCost),(i-nowDay))
    ans += min(c,nowCost)*(i-nowDay)
    nowCost += d[i]
    nowDay = i
print(ans)
#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
d = defaultdict(int)
for i in range(n) :
    d[a_n[i]] += 1
ans = []
for i in range(n) :
    if d[a_n[i]] == 1 :
        ans.append((a_n[i],i+1))
ret = -1
# print(a_n)
# print(d)
# print(ans)
if len(ans) > 0 :
    ret = max(ans)[1]
print(ret)
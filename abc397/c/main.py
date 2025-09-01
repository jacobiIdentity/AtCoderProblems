#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
d1 = defaultdict(int)
d1[a_n[0]] = 1
# d1Set = {a_n[0]}
d2 = defaultdict(int)
# d2Set = {a_n[i] for i in range(1,n)}
for i in range(1,n) :
    d2[a_n[i]] += 1
ans = len(d1)+len(d2)
for i in range(1,n) :
    d1[a_n[i]] += 1
    d2[a_n[i]] -= 1
    if d1[a_n[i]] == 0 : d1.pop(a_n[i])
    if d2[a_n[i]] == 0 : d2.pop(a_n[i])
    ans = max(ans,len(d1)+len(d2))
    # print(i,d1,d2,len(d1)+len(d2),ans)
print(ans)
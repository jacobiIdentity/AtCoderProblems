#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_3n = list(map(int, input().split()))
nTimes = [0]*(n+1)
d = defaultdict(int)
for i in range(3*n) :
    nTimes[a_3n[i]] += 1
    if nTimes[a_3n[i]] == 2 :
        d[a_3n[i]] = i
ans = list(map(lambda x:x[0], sorted(list(d.items()),key=lambda x:x[1])))
print(*ans)
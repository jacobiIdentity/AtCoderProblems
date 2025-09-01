#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n) :
    s = input()
    d[s] += 1
ans,cnt = '',0
for dd in d :
    if d[dd] > cnt :
        ans = dd
        cnt = d[dd]
print(ans)
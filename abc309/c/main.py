#!/usr/bin/env python3
from collections import defaultdict
n, k = map(int, input().split())
d = defaultdict(int)
for i in range(n) :
    a, b = map(int, input().split())
    d[a] += b
med, ans = 0, 1
for i, a in enumerate(sorted(d, reverse=True)) :
    med += d[a]
    if med > k :
        ans += a
        break
print(ans)
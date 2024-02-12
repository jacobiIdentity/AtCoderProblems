#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int, input().split()))
d = defaultdict(int)
for i in range(n) :
    d[a_n[i]] += 1
ans = 0
for i in d :
    ans += d[i]//2
print(ans)
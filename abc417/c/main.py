#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
d = defaultdict(set)
for i in range(n) :
    d[i+1+a_n[i]].add(i+1)
ans = 0
for j in range(n) :
    if j+1-a_n[j] in d :
        ans += len(d[j+1-a_n[j]])
print(ans)

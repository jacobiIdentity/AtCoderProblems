#!/usr/bin/env python3
from collections import defaultdict
n, q = map(int, input().split())
a_n = list(map(int, input().split()))
aDict = defaultdict(list)
for i in range(n) :
    aDict[a_n[i]].append(i+1)
for _ in range(q) :
    x, k = map(int, input().split())
    if len(aDict[x]) < k :
        print(-1)
    else :
        print(aDict[x][k-1])
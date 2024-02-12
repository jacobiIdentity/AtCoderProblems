#!/usr/bin/env python3
from collections import defaultdict
n, m = map(int, input().split())
h_n = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(m) :
    a, b = map(int ,input().split())
    d[a-1].append(b-1)
    d[b-1].append(a-1)
tmp = [i for i in range(n)]
ans = set()
while tmp :
    t = tmp.pop(-1)
    isGood = True
    for dd in d[t] :
        if h_n[t] <= h_n[dd] :
            isGood = False
            break
        elif dd in tmp :
            tmp.remove(dd)
    if isGood :
        ans.add(t)
        for dd in d[t] :
            if dd in tmp :
                tmp.remove(dd)
print(len(ans))
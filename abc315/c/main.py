#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
fs = set()
ices = defaultdict(list)
maxes = [0]*(n+1)
for _ in range(n) :
    f, s = map(int, input().split())
    fs.add(f)
    if len(ices[f]) == 0 :
        ices[f].append(s)
    elif len(ices[f]) == 1 :
        ices[f].append(s)
    else :
        t = min(ices[f]) 
        if t < s :
            ices[f].remove(t)
            ices[f].append(s)
    maxes[f] = max(maxes[f],s)
a = 0
for f in fs :
    # maxes[f] = max(ices[f])
    if len(ices[f]) == 1 :
        continue
    a = max(max(ices[f])+min(ices[f])//2, a)
a = max(a, sum(sorted(maxes, reverse=True)[0:2]))
print(a)
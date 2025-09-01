#!/usr/bin/env python3
from collections import defaultdict
import bisect
n = int(input())
d = defaultdict(set)
for i in range(n) :
    x,y = map(int,input().split())
    d[y].add((x,i))
s = input()
ans = 'No'
for y in d :
    if len(d[y]) < 2 : continue
    l = []
    r = []
    for x,i in d[y] :
        if s[i] == 'L':
            l.append(x)
        else :
            r.append(x)
    r.sort()
    for xl in l :
        pos = bisect.bisect_left(r,xl)
        if pos > 0 :
            ans = 'Yes'
print(ans)
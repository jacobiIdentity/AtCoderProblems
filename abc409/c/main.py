#!/usr/bin/env python3
from collections import defaultdict
n,l = map(int,input().split())
if l%3 :
    print(0)
    exit()
d_n = list(map(int,input().split()))
pos = 0
d = defaultdict(set)
d[pos].add(0)
for i in range(n-1) :
    pos += d_n[i]
    pos %= l
    d[pos].add(i+1)
ans = 0
for i in range(l//3) :
    if i in d and i+l//3 in d and i+2*l//3 in d :
        ans += len(d[i])*len(d[i+l//3])*len(d[i+2*l//3])
print(ans)
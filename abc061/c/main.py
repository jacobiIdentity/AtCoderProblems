#!/usr/bin/env python3
from collections import defaultdict
n,k = map(int,input().split())
d = defaultdict(int)
for _ in range(n) :
    a,b = map(int,input().split())
    d[a] += b
# print(d)
now = 0
d_keys = list(d.keys())
d_keys.sort()

for i in range(len(d_keys)) :
    now += d[d_keys[i]]
    if k <= now :
        print(d_keys[i])
        exit()
print(d_keys[-1])
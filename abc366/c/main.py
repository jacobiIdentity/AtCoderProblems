#!/usr/bin/env python3
from collections import defaultdict
d = defaultdict(int)
q = int(input())
box = set()
for _ in range(q):
    q = input()
    if q == '3':
        print(len(box))
        continue
    x = int(q[2:])
    if q[0] == '1' :
        d[x] += 1
        box.add(x)
    else :
        if d[x] == 1 :
            box.discard(x)
        d[x] -= 1

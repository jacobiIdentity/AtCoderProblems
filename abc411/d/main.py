#!/usr/bin/env python3
from collections import deque
n,q = map(int,input().split())
pcs = [-1 for _ in range(n+1)]
pcs[0] = 0
d = {0:''}
for _ in range(q) :
    c,*ps = input().split()
    p = int(ps[0])
    if c=='1' :
        pcs[p]=pcs[0]
    elif c=='2' :
        pcs.append(pcs[p])
        pcs[p] = len(pcs)-1
        d[len(pcs)-1] = ps[1]
    else :
        pcs[0] = pcs[p]
# print(pcs)
# print(d)
ans = deque()
now = 0
visited = set()
while now in d and now not in visited:
    ans.appendleft(d[now])
    visited.add(now)
    now = pcs[now]

print(''.join(ans))
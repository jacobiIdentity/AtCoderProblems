#!/usr/bin/env python3
from collections import defaultdict
h,w,n = map(int,input().split())
rows = defaultdict(set)
cols = defaultdict(set)
for _ in range(n) :
    x,y = map(int,input().split())
    rows[x].add(y)
    cols[y].add(x)
q = int(input())
for _ in range(q) :
    a,xy = map(int,input().split())
    if a== 1:
        print(len(rows[xy]))
        for i in rows[xy] :
            cols[i].discard(xy)
        rows.pop(xy)
    else :
        print(len(cols[xy]))
        for i in cols[xy]:
            rows[i].discard(xy)
        cols.pop(xy)


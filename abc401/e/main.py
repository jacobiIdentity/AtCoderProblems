#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(set)
for _ in range(m) :
    u,v = map(int,input().split())
    d[u-1].add(v-1)
    d[v-1].add(u-1)
isNg = False
vSet1 = set()
vSet2 = set()
for i in range(n) :
    if i == 0:
        if len(d[i]) == 0 :
            isNg =True
            print(0)
        else :
            vSet1 |= d[i]
            vSet2 |= d[i]
            print(len(vSet1))
    elif i not in d[i-1] :
        isNg = True
    if i>0 and isNg :
        print(-1)

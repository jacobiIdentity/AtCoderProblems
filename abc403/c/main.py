#!/usr/bin/env python3
from collections import defaultdict
n,m,q = map(int,input().split())
d = defaultdict(set)
for _ in range(q) :
    c,*x_y = map(int,input().split())
    if c==1 :
        x,y = x_y[0],x_y[1]
        d[x].add(y)
    elif c==2 :
        x = x_y[0]
        d[x].add(float('inf'))
    else :
        x,y = x_y[0],x_y[1]
        if y in d[x] or float('inf') in d[x] :
            print('Yes')
        else :
            print('No')

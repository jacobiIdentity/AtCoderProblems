#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
d = [0]*n
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1]+=1
    d[b-1]+=1
print(*d,sep="\n")
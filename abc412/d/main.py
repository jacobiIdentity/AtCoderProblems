#!/usr/bin/env python3
from collections import defaultdict
import heapq
d = defaultdict(set)
n,m = map(int,input().split())
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
lenleq1,len2,lengeq3 = [],[],[]
for i in range(n) :
    if len(d[i])<2 :
        lenleq1.append((-len(d[i]),i))
    elif len(d[i])>2 :
        lengeq3.append((len(d[i]),i))
    else :
        len2.append(i)
lenleq1.sort()
len2.sort()
lengeq3.sort()
print(lenleq1)
print(len2)
print(lengeq3)

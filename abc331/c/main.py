#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
cnts = defaultdict(int)
for a in a_n :
    cnts[a] += 1
s = sorted(list(set(a_n)), reverse=True)
d = defaultdict(int)
cnt = 0
for t in s :
    d[t] = cnt
    cnt += cnts[t]*t

for i in range(n) :
    print(d[a_n[i]], end=" " if i <n-1 else "\n")

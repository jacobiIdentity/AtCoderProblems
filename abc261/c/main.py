#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
s_n = [input() for _ in range(n)]
d = defaultdict(int)
for i in range(n) :
    if d[s_n[i]] == 0 :
        print(s_n[i])
    else :
        print(s_n[i]+'('+str(d[s_n[i]])+')')
    d[s_n[i]] += 1

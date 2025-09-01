#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
w_n = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n) :
    d[a_n[i]].append(w_n[i])
ans = 0
for i in d :
    if len(d[i]) > 1 :
        ans += (sum(d[i])-max(d[i]))
print(ans)
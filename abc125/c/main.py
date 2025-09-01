#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
d2 = defaultdict(int)
for i in range(n) :
    t = 1
    while t*t<= a_n[i] :
        if a_n[i]%t==0 :
            d2[t] += 1
            if t != a_n[i]//t :
                d2[a_n[i]//t] += 1
        t+=1
ans = 1
for dd in d2 :
    if d2[dd] > n-2 :
        ans = max(ans,dd)
print(ans)
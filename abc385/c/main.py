#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
h_n = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n) :
    d[h_n[i]].append(i)
ans = 1
for i in range(n) :
    # for j in range(1,n-i) :
    for j in reversed(sorted(d[h_n[i]])) :
        if j <= i : break
        tmp = 1
        now = j
        while now < n :
            if now in d[h_n[i]] :
                tmp += 1
                now += (j-i)
            else :
                break
        ans = max(tmp,ans)  
print(ans)
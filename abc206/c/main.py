#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
# d = defaultdict(set)
d = defaultdict(int)
for i in range(n) :
    # d[a_n[i]].add(i)
    d[a_n[i]] += 1
ans = (n*(n-1))//2
for i in d :
    # ans -= (len(d[i])*(len(d[i])-1))//2
    ans -= (d[i]*(d[i]-1))//2
print(ans)
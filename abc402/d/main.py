#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
pararells = [0]*n
for i in range(m) :
    a,b = map(int,input().split())
    pararells[(a+b)%n] += 1
ans = m*(m-1)//2
ans -= sum([p*(p-1)//2 for p in pararells])
print(ans)
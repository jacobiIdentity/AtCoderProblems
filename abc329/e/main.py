#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int, input().split())
s = input()
t = input()
tLenSet = defaultdict(set)
tLenSet[m].add(t)
for i in range(m+1,n+1) :
    for j in range(1,i-m+1) :
        for tt in tLenSet[i-j] :
            tLenSet[i].add(t[:j]+tt)
            tLenSet[i].add(tt+t[-j:])
print(tLenSet)

print('Yes' if s in tLenSet[n] else 'No')
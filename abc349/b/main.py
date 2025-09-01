#!/usr/bin/env python3
from collections import defaultdict
s = input()
d = defaultdict(set)

for a in 'abcdefghijklmnopqrstuvwxyz' :
    if s.count(a) > 0 :
        d[s.count(a)].add(a)
isYes = True
for i in d :
    if len(d[i]) != 0 and len(d[i]) != 2 :
        isYes = False
print('Yes' if isYes else 'No')
# print(d)
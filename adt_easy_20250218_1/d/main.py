#!/usr/bin/env python3
from collections import defaultdict
s = input()
d = defaultdict(set)
for i in range(26) :
    d[s.count(chr(ord('a')+i))].add(i)
isYes = True
# print(d)
for i,v in d.items() :
    if i>0 and len(v)!= 0 and len(v) != 2 :
        isYes = False
print('YNeos'[not(isYes)::2])
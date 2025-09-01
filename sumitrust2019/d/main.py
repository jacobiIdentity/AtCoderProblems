#!/usr/bin/env python3
import itertools
n = int(input())
s = input()
ans = set()
d1 = dict()
d2 = dict()
for i in range(n) :
    for dd in d2 :
        ans.add(dd+s[i])
    for d in d1 :
        if d+s[i] not in d2 :
            d2[d+s[i]]= i
    if s[i] not in d1 :
        d1[s[i]] = i
print(len(ans))

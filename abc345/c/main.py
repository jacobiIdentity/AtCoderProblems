#!/usr/bin/env python3
from collections import defaultdict
s = input()
d = defaultdict(int)
sLen = len(s)
dupSet = set()
for i in range(sLen) :
    d[s[i]] += 1
    if d[s[i]] > 1 :
        dupSet.add(s[i])
duplicateCnt = 0
for t in dupSet :
    if d[t] > 2 or (len(dupSet) > 1 and  d[t] > 1):
        duplicateCnt += (d[t]*(d[t]-1))//2
if duplicateCnt == 0 :
    duplicateCnt = 1
print((sLen*(sLen-1)//2-duplicateCnt+1))

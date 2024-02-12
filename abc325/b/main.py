#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
pDict = defaultdict(int)
tDict = defaultdict(set)
peopleCntList = [0]*24
for i in range(n) :
    pDict[i], t = map(int, input().split())
    tDict[i] = {(t+j)%24 for j in range(9, 18)}
for i in range(n) :
    for j in range(24) :
        if j in tDict[i] :
            peopleCntList[j] += pDict[i]
print(max(peopleCntList))
# print(tDict)
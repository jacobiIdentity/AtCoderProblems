#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = sorted(list(map(int, input().split())))
aSetList = sorted(list(set(a_n)))
aDict = defaultdict(int)
for i in range(n) :
    aDict[a_n[i]] += 1
dList = sorted(aDict)
print(dList)
print(aDict)

now,  l = 1, len(a_n)
while now < n :
    if len(aSetList) < 1 : break
    if aSetList[0] != now :
        if amari +len(aSetList) < 2 : break
        elif amari > 1 : amari -= 2
        elif amari == 1 :
            amari -= 1
            aSetList.pop(-1)
        elif amari > 1 :
            amari -= 2
        else :
            aSetList.pop(-1)
            aSetList.pop(-1)
    else :
        if len(aSetList) == 1 and amari > 0 :
            amari -= 2
        else :
            aSetList.pop(0)
    # print(aSetList)
    now += 1
print(now-1)
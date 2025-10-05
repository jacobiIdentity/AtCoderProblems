#!/usr/bin/env python3
import heapq
n,q = map(int,input().split())
versionCnt = [0]+[1]*n
minVer = 1
for i in range(q) :
    x,y = map(int,input().split())
    ret = 0
    while minVer <= x :
        ret += versionCnt[minVer]
        versionCnt[y] += versionCnt[minVer]
        minVer += 1
    print(ret)

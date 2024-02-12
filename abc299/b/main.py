#!/usr/bin/env python3
n, t = map(int, input().split())
c_n = list(map(int, input().split()))
r_n = list(map(int, input().split()))
tMax, tNum, p1Max , p1Num = -1, -1, -1, -1
for i in range(n) :
    if c_n[i] == t :
        tNum = i if r_n[i] > tMax else tNum
        tMax = r_n[i] if r_n[i] > tMax else tMax
    if c_n[i] == c_n[0] :
        p1Num = i if r_n[i] > p1Max else p1Num
        p1Max = r_n[i] if r_n[i] > p1Max else p1Max
print((tNum+1) if tMax != -1 else (p1Num+1))
    

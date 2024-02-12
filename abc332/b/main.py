#!/usr/bin/env python3

k,g,m = map(int ,input().split())
tmpG, tmpM = 0, 0
for _ in range(k) :
    if tmpG == g :
        tmpG = 0
    elif tmpM == 0 :
        tmpM = m
    else :
        diff = min(g-tmpG, tmpM)
        tmpG += diff
        tmpM -= diff
print(tmpG, tmpM)
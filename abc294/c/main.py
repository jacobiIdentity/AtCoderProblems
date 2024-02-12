#!/usr/bin/env python3
from collections import deque
n, m = map(int, input().split())
aq = deque(map(int, input().split()))
bq = deque(map(int, input().split()))
aOrder = [0]*n
bOrder = [0]*m
a, b, aCnt, bCnt, i = aq.popleft(), bq.popleft(), 0, 0, 1
while i < n+m+1 :
    if aCnt == n :
        bOrder[bCnt] = i
        bCnt += 1
    elif bCnt == m :
        aOrder[aCnt] = i
        aCnt += 1
    elif a < b :
        aOrder[aCnt] = i
        aCnt += 1
        if aq :
            a = aq.popleft()
    else :
        bOrder[bCnt] = i
        bCnt += 1
        if bq :
            b = bq.popleft()
    i += 1
print(*aOrder)
print(*bOrder)
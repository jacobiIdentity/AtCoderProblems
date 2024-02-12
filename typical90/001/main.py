#!/usr/bin/env python3
import math
from collections import deque
n, l = map(int, input().split())
k = int(input())
a_n = list(map(int, input().split()))
left, right = 0, l
mid = (left+right)//2
while left <= right :
    cnt, before = 0, 0
    for i in range(n) :
        tmp = a_n[i] - before
        if tmp >= mid :
            before = a_n[i]
            cnt += 1
    cnt += 1 if l -before >= mid else 0
    # print(left, right, mid, cnt, before)
    if cnt >= k+1 :
        left = mid + 1
    else :
        right = mid -1
    mid = (left+right)//2
print(mid)
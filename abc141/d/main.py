#!/usr/bin/env python3
import heapq
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
que = []
heapq.heapify(que)
cnt = 0
for i in range(n) :
    heapq.heappush(que,-a_n[i])
while cnt < m :
    mA = heapq.heappop(que)
    cnt += 1
    mA *= -1
    mA //= 2
    heapq.heappush(que,-mA)
print(-sum(que))
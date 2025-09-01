#!/usr/bin/env python3
import heapq
n,k = map(int,input().split())
p_n = list(map(int,input().split()))
que = []
heapq.heapify(que)
for i in range(k) :
    heapq.heappush(que,p_n[i])
for i in range(k-1,n) :
    t = heapq.heappop(que)
    print(t)
    if i < n-1 :
        t = max(t,p_n[i+1])
        heapq.heappush(que,t)

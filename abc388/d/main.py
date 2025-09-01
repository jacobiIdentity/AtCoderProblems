#!/usr/bin/env python3
import heapq
n = int(input())
a_n = list(map(int,input().split()))
que = []
heapq.heapify(que)
b_n = []
for i in range(n) :
    tmp = -1
    if que :
        tmp = heapq.heappop(que)
    if tmp < i :
        while que :
            tmp = heapq.heappop(que)
            if tmp >= i :
                break
    if tmp >= i :
        heapq.heappush(que,tmp)
    b_n.append(max(0,a_n[i]-(n-i-1)+len(que)))
    heapq.heappush(que,a_n[i]+i+len(que))
print(*b_n)    

#!/usr/bin/env python3
import heapq
q = int(input())
heap = []
for _ in range(q) :
    query = list(map(int,input().split()))
    if query[0]== 1 :
        heapq.heappush(heap,query[1])
    else :
        print(heapq.heappop(heap))
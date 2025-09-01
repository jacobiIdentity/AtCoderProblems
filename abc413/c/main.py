#!/usr/bin/env python3
import heapq
q = int(input())
now = 0
que = []
for _ in range(q) :
    query = list(map(int,input().split()))
    if query[0]==1 :
        heapq.heappush(que,(now,query[1],query[2]))
        now += 1
    else :
        k=query[1]
        ans = 0
        while que :
            i,c,x = heapq.heappop(que)
            if c<k :
                ans += c*x
                k -= c
                continue
            print(ans+ k*x)
            heapq.heappush(que,(i,c-k,x))
            break


#!/usr/bin/env python3
import heapq
n,q = map(int,input().split())
nowVersion = list(range(n + 1))
que = []
for i in range(1,n+1) :
    heapq.heappush(que,(i,1))
for i in range(q) :
    x,y = map(int,input().split())
    ret = 0
    while que :
        version,cnt = heapq.heappop(que)
        if version > x:
            heapq.heappush(que,(version,cnt))
            break
        ret += cnt
    print(ret)
    heapq.heappush(que,(y,ret))
    # print(que)
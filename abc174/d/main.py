#!/usr/bin/env python3
from collections import defaultdict
import heapq
n = int(input())
c_i = list(input())
# print(c_i)
wq,rq = [],[]
ngs = set()
heapq.heapify(wq)
heapq.heapify(rq)
for i in range(n) :
    if c_i[i]=='W' :
        heapq.heappush(wq,i)
    if c_i[i]=='R' :
        heapq.heappush(rq,-i)
    if 0<=i-1<n and c_i[i-1]=='W' and c_i[i]=='R' :
        ngs.add(i-1)
# print(wq)
# print(rq)
# print(ngs)
ans = 0
while wq and rq and ngs :
    w1 = heapq.heappop(wq)
    r1 = -heapq.heappop(rq)
    # print()
    # print(w1,r1,ans)
    c_i[w1],c_i[r1] = c_i[r1],c_i[w1]
    if 0<=w1+1<n and not(c_i[w1]=='W' and c_i[w1+1]=='R') :
        ngs.discard(w1)
    if 0<=r1-1<n and not(c_i[r1-1]=='W' and c_i[r1]=='R') :
        ngs.discard(r1-1)
    if 0<=w1-1<n and (c_i[w1-1]=='W' and c_i[w1]=='R') :
        ngs.add(w1-1)
    if 0<=r1+1<n and (c_i[r1]=='W' and c_i[r1+1]=='R') :
        ngs.add(r1)
    heapq.heappush(wq,r1)
    heapq.heappush(rq,-w1)
    ans += 1
    # print(c_i)
    # print(wq)
    # print(rq)
    # print(ngs)
print(ans)
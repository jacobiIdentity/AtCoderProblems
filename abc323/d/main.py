#!/usr/bin/env python3
from collections import defaultdict
import heapq
n = int(input())
d = defaultdict(int)
q = []
qSet = set()
heapq.heapify(q)
ans = 0
for _ in range(n) :
    s,c = map(int,input().split())
    if s%2== 1 :
        ans += c%2
        if c//2 == 0 :
            continue
        d[s*2] += c//2
        s *= 2
    else :
        d[s] += c
    if s not in qSet :
        heapq.heappush(q,s)
    qSet.add(s)
# print(qSet,q,d,ans)
while q :
    s = heapq.heappop(q)
    ans += d[s]%2
    d[s*2] += d[s]//2
    if d[s*2]>0 and 2*s not in qSet :
        heapq.heappush(q,2*s)
    qSet.discard(s)
print(ans)
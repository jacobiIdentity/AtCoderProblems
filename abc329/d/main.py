#!/usr/bin/env python3
import heapq
from collections import defaultdict
n,m = map(int, input().split())
a_n = list(map(int, input().split()))
d = defaultdict(int)
ans = []
heapq.heapify(ans)
for i in range(m) :
    d[a_n[i]] += 1
    heapq.heappush(ans,(-d[a_n[i]],a_n[i]))
    ma,a = heapq.heappop(ans)
    print(a)
    heapq.heappush(ans,(ma,a))

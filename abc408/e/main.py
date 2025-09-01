#!/usr/bin/env python3
import heapq
from collections import defaultdict
n,m = map(int,input().split())
d1 = defaultdict(int)
d2 = defaultdict(set)
for _ in range(m) :
    u,v,w = map(int,input().split())
    d2[u-1].add((v-1,w))
    d2[v-1].add((u-1,w))
que = []
heapq.heappush(que,(0,0))
visited = [float('inf')]*n
visited[0] = 0
while que :
    w,u = heapq.heappop(que)
    if u==n-1 :
        print(visited[-1])
        print(visited)
        exit()
    if visited[u]<w :
        continue
    for v2,w2 in d2[u] :
        if w|w2 < visited[v2] :
            visited[v2] = w|w2
            que.append((w|w2,v2))
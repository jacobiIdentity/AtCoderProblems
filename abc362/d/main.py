#!/usr/bin/env python3
import heapq
n,m = map(int,input().split())
a_i = list(map(int,input().split()))
g = [[] for _ in range(n)]
for _ in range(m) :
    u,v,b = map(int,input().split())
    g[u-1].append([b,v-1])
    g[v-1].append([b,u-1])

d = [float('inf')]*n
d[0] = a_i[0]
# used = [False]*n
# used[s] = True
que = []
heapq.heappush(que, (a_i[0],0))
while que :
    c, v = heapq.heappop(que)
    if d[v] < c :
        continue
    for cost, t in g[v] :
        if d[v]+a_i[t]+cost < d[t] :
            d[t] = d[v]+a_i[t]+cost
            heapq.heappush(que,(d[t], t))
print(*d[1:])

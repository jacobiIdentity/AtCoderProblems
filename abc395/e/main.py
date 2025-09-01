#!/usr/bin/env python3
from collections import deque,defaultdict
import heapq
n,m,x = map(int,input().split())
d1  = defaultdict(set)
d2  = defaultdict(set)
for _ in range(m) :
    u,v = map(int,input().split())
    d1[u-1].add(v-1)
    d2[v-1].add(u-1)
visited = [float('inf')]*n
visited[0] = 0
h = []
heapq.heapify(h)
heapq.heappush(h,(0,True))
while h :
    v1,isD1 = heapq.heappop(h)

# q = deque()
# q.append((0,0,True))
# while q :
#     v1,cost,isD1 = q.popleft()
#     if visited[v1] < cost :
#         continue
#     visited[v1] = cost
    # if v1 == n-1 :
    #     continue
    dlow,dhigh = d1,d2
    if not(isD1) :
        dlow,dhigh = dhigh,dlow
    for v2 in dlow[v1] :
        if visited[v1]+1 < visited[v2] :
            visited[v2] = visited[v1]+1
            heapq.heappush(h,(v2,isD1))
        # q.append((v2,cost+1,isD1))
    for v2 in dhigh[v1] :
        if visited[v1]+1+x < visited[v2] :
            visited[v2] = visited[v1]+1+x
            heapq.heappush(h,(v2,not(isD1)))
        # if visited[v2] < cost+1+x :
        #     continue
#         q.append((v2,cost+1+x,not(isD1)))
print(visited[n-1])
# print(visited)
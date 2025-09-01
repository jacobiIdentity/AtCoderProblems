#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
d = defaultdict(set)
weight = defaultdict(int)
for i in range(m) :
    u,v,w = map(int,input().split())
    weight[(u-1,v-1)] = w
    weight[(v-1,u-1)] = -w
    d[u-1].add(v-1)
    d[v-1].add(u-1)
ans = [0]*n
visited = [False]*n
for i in range(n) :
    if visited[i] : continue 
    visited[i] = True
    que = deque()
    que.append(i)
    while que :
        v1 = que.popleft()
        for v2 in d[v1] :
            if visited[v2] :continue
            que.append(v2)
            visited[v2] = True
            ans[v2] = ans[v1] + weight[(v1,v2)]
print(*ans,sep=" ")
#!/usr/bin/env python3
from collections import deque,defaultdict
n = int(input())
graph = defaultdict(set)
for _ in range(n-1) :
    a,b = map(int,input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)
ans = 0
for i in range(n) :
    visited = [-1]*n
    tmp = 0
    que = deque()
    que.append((i,0))
    while que :
        v1,tmp = que.popleft()
        ans = max(ans,tmp+1)
        if visited[v1] > -1 :
            continue
        visited[v1] = tmp
        for v2 in graph[v1] :
            que.append((v2,tmp+1))
print(ans)
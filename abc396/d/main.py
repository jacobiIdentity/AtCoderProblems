#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
que = deque()
que.append((1,{1},0))
ans = float('inf')
while que :
    v,path,val = que.popleft()
    if v == n :
        ans = min(ans,val)
        continue
    for w,val2 in graph[v] :
        if w not in path :
            que.append((w,path|{w},val^val2))

print(ans)
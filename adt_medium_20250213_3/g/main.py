#!/usr/bin/env python3
from collections import deque,defaultdict
n = int(input())
d = defaultdict(set)
for _ in range(n-1) :
    u,v = map(int,input().split())
    d[u-1].add(v-1)
    d[v-1].add(u-1)
q = deque()
q.append((0,1))
ans = float('inf')
visited = [False]*n
while q :
    v1,cnt = q.popleft()
    if visited[v1] :
        continue
    visited[v1] = True
    if len(d[v1]) == 1 :
        ans = min(ans,cnt)
        continue
    for v2 in d[v1] :
        print((v2+1,cnt+len(d[v2])))
        q.append((v2,cnt+len(d[v2])))
print(cnt)
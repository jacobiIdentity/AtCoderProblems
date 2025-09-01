#!/usr/bin/env python3
from collections import defaultdict, deque
n, m = map(int, input().split())
d = defaultdict(set)
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
ans = 0
visited = [False]*n
for i in range(n) :
    if visited[i] : continue
    visited[i] = True
    vertexes = {i}
    edges = set()
    que = deque()
    que.append(i)
    while que :
        v = que.popleft()
        for w in d[v] :
            edges.add((w,v))
            edges.add((v,w))
            vertexes.add(w)
            if visited[w] : continue
            visited[w] = True
            que.append(w)
    ans += (len(vertexes)*(len(vertexes)-1))//2 - len(edges)//2
print(ans)

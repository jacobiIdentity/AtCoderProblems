#!/usr/bin/env python3
from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(set)
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
ans = set()
for i in range(n) :
    visited = [0]*n
    que = deque()
    que.append(i)
    while que :
        v = que.popleft()
        visited[v] = 1
        ans.add((i,v))
        for w in d[v] :
            if visited[w] :
                continue
            que.append(w)

print(len(ans))
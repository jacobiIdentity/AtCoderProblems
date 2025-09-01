#!/usr/bin/env python3
from collections import defaultdict,deque
# import heapq
n,m = map(int,input().split())
d = defaultdict(set)
for _ in range(m) :
    a,b,w = map(int,input().split())
    d[a-1].add((b-1,w))
    # d[b-1].add((a-1,w))
visited = [set() for _ in range(n)]
visited[0].add(0)
# que = []
que = deque([(0,0)])
while que :
    a,c = que.popleft()
    for b,w in d[a]:
        if c^w in visited[b] :
            continue
        visited[b].add(c^w)
        que.append((b,c^w))
# print(visited)
if len(visited[-1])==0 :
    print(-1)
else :
    print(min(visited[-1]))

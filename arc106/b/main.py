#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
graph = defaultdict(set)
for _ in range(m) :
    c,d = map(int,input().split())
    graph[c-1].add(d-1)
    graph[d-1].add(c-1)
visited = [False]*n
isYes = True
for i in range(n) :
    if visited[i] : continue
    q = deque()
    q.append(i)
    cc_a = 0
    cc_b = 0
    while q :
        v = q.popleft()
        if visited[v] : continue
        visited[v] = True
        cc_a += a_n[v]
        cc_b += b_n[v]
        for w in graph[v] :
            if not(visited[w]) : q.append(w)
    if cc_a != cc_b :
        isYes = False
        break
print('Yes' if isYes else 'No')

    
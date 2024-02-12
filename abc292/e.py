#!/usr/bin/env python3
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m) :
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
ans = 0
que = deque()
for i in range(n) :
    visited = [False]*n
    visited[i] = True
    que.append(i)
    while len(que) > 0 :
        now = que.popleft()
        for j in graph[now] :
            if visited[j] : continue
            visited[j] = True
            que.append(j)
            ans += 1
        # print(ans)
print(ans-m)

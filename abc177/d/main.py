#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
n,m = map(int, input().split())
d = defaultdict(set)
for _ in range(m) :
    a,b = map(int, input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
ans = 0
visited = [0]*n
# print(d)
q = deque()
for i in range(n) :
    if visited[i] :
        continue
    q.append(i)
    visited[i] = 1
    tmp = 1
    while q :
        v = q.popleft()
        for w in d[v] :
            if not(visited[w]) :
                tmp += 1
                visited[w] = 1
                q.append(w)
    # print(i,tmp)
    ans = max(ans,tmp)
print(ans)
#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
d = defaultdict(set)
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
visited = [-1]*n
que = deque()
que.append(0)
visited[0] = 0
isYes = False
while que :
    v = que.popleft()
    for w in d[v] :
        if visited[w] == -1 :
            visited[w] = visited[v]+1
            d[w].discard(v)
            que.append(w)
        elif abs(visited[w]-visited[v]) > 0 : 
            print(visited[v]+visited[w]+1)
            exit()
print(-1)
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
while que :
    v = que.popleft()
    for w in d[v] :
        if visited[w]==-1 :
            visited[w] = v
            que.append(w)
# print(visited)
isNo = False
for i in range(n) :
    if visited[i] == -1 :
        isNo = True
        break
print('YNeos'[isNo::2])
if not(isNo) :
    for i in range(1,n) :
        print(visited[i]+1)

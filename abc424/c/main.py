#!/usr/bin/env python3
from collections import deque,defaultdict
n = int(input())
d = defaultdict(set)
que = deque()
visited = [0]*n
for i in range(n) :
    a,b = map(int,input().split())
    if a==b==0 :
        que.append(i)
        visited[i] = 1
    else :
        if a-1 != i :
            d[a-1].add(i)
        if b-1 != i :
            d[b-1].add(i)
# print(que)
# print(d)
while que :
    v = que.popleft()
    for w in d[v] :
        if visited[w]==0 :
            visited[w] = 1
            que.append(w)
print(sum(visited))
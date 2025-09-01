#!/usr/bin/env python3
from collections import deque
n,k = map(int,input().split())
a_n =list(map(int,input().split())) 
visited = [-1]*n
q = deque()
q.append(0)
cnt = 0
while q :
    v = q.popleft()
    if visited[v] != -1 :
        break
    visited[v] = cnt
    cnt += 1
    q.append(a_n[v]-1)
# print(v,cnt,visited)
if k <= visited[v] :
    print(visited.index(k)+1)
else :
    print(visited.index((k-visited[v])%(cnt-visited[v])+visited[v])+1)
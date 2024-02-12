#!/usr/bin/env python3
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m) :
    a, b, x, y = map(int, input().split())
    if (b-1,x,y) not in graph[a-1] :
        graph[a-1].append((b-1,x,y))
    if (a-1,-x,-y) not in graph[b-1] :
        graph[b-1].append((a-1,-x,-y))
q = deque()
visited = [True]+[False]*(n-1)
ans = [(0,0)]*n
q.append(0)
while q :
    i = q.popleft()
    for j,xx,yy in graph[i] :
        if not(visited[j]) :
            q.append(j)
            visited[j] = True
            ans[j] = (ans[i][0]+xx,ans[i][1]+yy)
for i in range(n) :
    if not(visited[i]) :
        print('undecidable')
    else :
        print(ans[i][0],ans[i][1])
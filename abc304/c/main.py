#!/usr/bin/env python3
from collections import defaultdict, deque
def length(i, j) :
    dx = grid[i][0] - grid[j][0]
    dy = grid[i][1] - grid[j][1]
    return(dx*dx+dy*dy)
n, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
neighbor = defaultdict(set)
for i in range(n) :
    for j in range(i+1, n) :
        if length(i,j) < d*d + 1 :
            neighbor[i].add(j)
            neighbor[j].add(i)
q = deque()
visited = [False]*n
q.append(0)
ans = {0}
while q :
    tmp = q.popleft()
    visited[tmp] = True
    for i in neighbor[tmp] :
        if not(visited[i]) :
            ans.add(i)
            visited[i] = True
            q.append(i)
for i in range(n) :
    print('Yes' if i in ans else 'No')

#!/usr/bin/env python3
from collections import defaultdict,deque
n,x,y = map(int,input().split())
d = defaultdict(set)
for i in range(n-1) :
    d[i].add(i+1)
    d[i+1].add(i)
d[x-1].add(y-1)
d[y-1].add(x-1)
d2 = defaultdict(int)
# d3 = defaultdict(set)
for i in range(n-1) :
    visited = [0]*n
    que = deque()
    que.append(i)
    visited[i] = 1
    while que :
        v = que.popleft()
        for w in d[v] :
            if visited[w] == 0 :
                if i < w :
                    d2[visited[v]] += 1
                    # d3[visited[v]].add((i,w))
                visited[w] = visited[v]+1
                que.append(w)
    # print(visited)
for i in range(1,n) :
    print(d2[i])
    # print(d3[i])




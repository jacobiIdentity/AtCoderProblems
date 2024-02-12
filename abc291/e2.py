#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)
def dfs(x) :
    if lengths[x] != -1 : return lengths[x]
    lengths[x] = 0
    if not(graph[x] ): return lengths[x]
    for xx in graph[x] :
        lengths[x]=max(lengths[x],dfs(xx)+1)
    return lengths[x]
n, m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m) :
    x, y = map(int,input().split())
    graph[x-1].append(y-1)
lengths = [-1]*n
d = 0
for i in range(n) :
    d = max(d, dfs(i))
if d == n-1 :
    print('Yes')
    print(*[n-i for i in lengths])
else :
    print('No')
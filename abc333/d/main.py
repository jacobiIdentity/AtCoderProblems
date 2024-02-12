#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1) :
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
times = [-1]*n
times[0] = 0
def dfs(x) :
    tmp = 1
    for u in graph[x] :
        if times[u] == -1 and len(graph[u]) == 1 :
            times[u] = 1
        elif times[u] == -1 :
            times[u] = 0
            dfs(u)
        tmp += times[u]
    times[x] = tmp
maxB = 1
for i in graph[0] :
    times[i] = 0
    dfs(i)
    maxB = max(maxB, times[i])
print(n-maxB)
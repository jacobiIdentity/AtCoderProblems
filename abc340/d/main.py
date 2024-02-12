#!/usr/bin/env python3
import heapq
n = int(input())
graph = dict()
for i in range(n-1) :
    a,b,x = map(int, input().split())
    if i+1 == x-1 :
        graph[i] = {i+1:min(a,b)}
    else :
        graph[i]= {i+1:a, x-1:b}
graph[n-1] = {}
# print(graph)
d = [float("Inf")]*n
d[0] = 0
visited = [0]*n
que = []
heapq.heappush(que,(0,0))
while que :
    c,s = heapq.heappop(que)
    if visited[s] :
        continue
    visited[s] = 1
    d[s] = c
    for v in graph[s] :
        if not(visited[v]) and d[v] > d[s] + graph[s][v] :
            d[v] = d[s] + graph[s][v]
            heapq.heappush(que,(d[s] + graph[s][v],v))
            # print(s,v,d)
print(d[n-1])
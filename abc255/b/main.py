#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
graph = [tuple(map(int,input().split())) for _ in range(n)]
mins = [float('inf')]*n
for a in a_n :
    for i in range(n) :
        mins[i] = min(mins[i],(graph[a-1][0]-graph[i][0])**2+(graph[a-1][1]-graph[i][1])**2)
print(max(mins)**0.5)
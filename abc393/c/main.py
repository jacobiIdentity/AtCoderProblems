#!/usr/bin/env python3
n,m = map(int,input().split())
graph = set()
ans = 0
for _ in range(m) :
    u,v = map(int,input().split())
    if u > v : u,v = v,u
    if u == v :
        ans += 1
        continue
    if (u,v) in graph :
        ans += 1
    graph.add((u,v))
print(ans)
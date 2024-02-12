#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
graph = dict()
for i in range(n) :
    graph[a_n[i]] = i+1
now = -1
for i in range(n) :
    if i == n-1 :
        print(graph[now])
    else :
        print(graph[now],end=" ")
        now = graph[now]
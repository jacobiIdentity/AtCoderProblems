#!/usr/bin/env python3
n = int(input())
graph = [[0]*100 for _ in range(100)]
for _ in range(n) :
    a, b, c, d = map(int, input().split())
    for i in range(a,b) :
        for j in range(c,d) :
            graph[i][j] = 1
print(sum(map(lambda x:sum(x), graph)))
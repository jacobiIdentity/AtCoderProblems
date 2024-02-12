#!/usr/bin/env python3
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

h, w = map(int, input().split())
graph = [input() for _ in range(h)]
sensors = set()
sensorsNumber = dict()
cnt = 0
for i in range(h) :
    for j in range(w) :
        if graph[i][j] == '#' :
            sensors.add((i,j))
            sensorsNumber[(i,j)] = cnt
            cnt += 1
uf = UnionFind(len(sensors))
for (i,j) in sensors :
    for k in range(max(0, i-1), min(i+2, h)) :
        for l in range(max(0, j-1), min(j+2, w)) :
                if (k,l) in sensors :
                    uf.union(sensorsNumber[(i,j)], sensorsNumber[(k,l)])
print(uf.group_count())


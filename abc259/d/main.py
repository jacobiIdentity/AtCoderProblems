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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
n = int(input())
sx,sy,gx,gy = map(int,input().split())
uf = UnionFind(n)
cs = [list(map(int,input().split())) for _ in range(n)]
s,g = 0,0
for i in range(n) :
    x,y,r = cs[i][0],cs[i][1],cs[i][2]
    if (sx-x)**2+(sy-y)**2 == r**2 :
        s = i
    if (gx-x)**2+(gy-y)**2 == r**2 :
        g = i
for i in range(n) :
    x1,y1,r1 = cs[i][0],cs[i][1],cs[i][2]
    for j in range(i+1,n) :
        x2,y2,r2 = cs[j][0],cs[j][1],cs[j][2]
        if (r1-r2)**2 <= (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2 :
            uf.union(i,j)
print('YNeos'[not(uf.same(s,g))::2])
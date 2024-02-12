#!/usr/bin/env python3
#https://output-zakki.com/unionfind/
#https://qiita.com/Waaaa1471/items/9b9f231a8b549ef60862
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        self.size = [1]*n
    def root(self, x) :
        if self.parents[x] == -1 :
            return x
        else :
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    def isSame(self, x, y) :
        return self.root(x) == self.root(y)
    def unite(self, x, y) :
        x = self.root(x)
        y = self.root(y)
        if x == y : return
        if self.size[x] < self.size[y] :
            x, y = y, x
        self.parents[y] = x
        self.size[x] += self.size[y]
    def Size(self, x) :
        return self.size[self.root(x)]

n,m = map(int, input().split())
uf = UnionFind(n)
x = 0
for _ in range(m) :
    a, b, c, d = input().split()
    a, c = int(a)-1, int(c)-1
    if uf.isSame(a, c) : 
        x += 1
    uf.unite(a, c)
y = 0
for i in range(n) :
    if uf.parents[i] == -1 :
        y += 1
print(x, y-x)
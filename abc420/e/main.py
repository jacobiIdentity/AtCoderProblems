#!/usr/bin/env python3
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.bPointCnt = [0]*n # 今回用変数 黒点の数を保持. parentの黒点の数のみ正しい
        
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
        self.bPointCnt[x] += self.bPointCnt[y]
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 今回用関数 黒点の数を変更する
    def addBPointCnt(self,x,state) :
        x = self.find(x)
        if state : #blackに変化
            self.bPointCnt[x] += 1
        else : #white に変化
            self.bPointCnt[x] -= 1
    
    # 今回用関数 連結成分の黒点の数が1以上かチェック
    def getReachBPoint(self,x) :
        return self.bPointCnt[self.find(x)]>0
    

n,q = map(int,input().split())
uf = UnionFind(n)
colors = [0]*n
for _ in range(q) :
    i,*uv = map(int,input().split())
    if i==1 :
        uf.union(uv[0]-1,uv[1]-1)
    if i==2 :
        colors[uv[0]-1] = 1-colors[uv[0]-1]
        uf.addBPointCnt(uv[0]-1,colors[uv[0]-1])
    if i==3 :
        print('YNeos'[not(uf.getReachBPoint(uv[0]-1))::2])

#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(set)
for _ in range(m):
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
stack = []
# 遷移元
prev = [-1]*n
# 訪問済みチェック
visited = [False]*n
isYes = True
for i in range(n) :
    if len(d[i]) >2 : 
        isYes = False
        break
    if visited[i] : continue
    stack.append((i,-1))
    while stack :
        v,last = stack.pop()
        if last != -1 : prev[v] = last
        visited[v] = True
        for w in d[v] :
            if w == last : continue
            if visited[w] :
                isYes = False
                break
            stack.append((w,v))
        
        if not(isYes) : break
    if not(isYes) : break
print('YNeos'[not(isYes)::2])

#!/usr/bin/env python3
from collections import defaultdict,deque

n = int(input())
inDegree = defaultdict(int)
d = defaultdict(set)
for i in range(n) :
    c,*p = map(int,input().split())
    for j in range(c) :
        inDegree[p[j]-1] +=1
        d[i].add(p[j]-1)
# print(d)
# print(inDegree)
que = deque()
que.append(0)
vSet = set()
while que :
    v = que.popleft()
    vSet.add(v)
    for w in d[v] :
        if w in vSet :
            continue
        que.append(w)
# print(vSet)
for i in range(n) :
    if inDegree[i] == 0 :
        que.append(i)
# print(que)
t = []
while que :
    v = que.popleft()
    t.append(v)
    for w in d[v] :
        inDegree[w] -= 1
        if inDegree[w] == 0 :
            que.append(w)
order = {t[i]:-i for i in range(n)}
# print(order)
ans = []
for i in range(n) :
    if i in vSet :
        ans.append(i+1)
ans.sort(key= lambda x: order[x-1])
ans.pop()
print(*ans)


#!/usr/bin/env python3
from collections import defaultdict,deque
n = int(input())
x,y = input().split()
sToI = {x:0,y:1}
now = 2
# next = defaultdict(set)
next = defaultdict(list)
for _ in range(n) :
    s,t = input().split()
    if s not in sToI :
        sToI[s] = now
        now += 1
    if t not in sToI :
        sToI[t] = now
        now += 1
    next[sToI[s]].append(sToI[t])
    # next[sToI[s]].add(sToI[t])
    # next[s].add(t)
visited = [False]*(now)
# visited = defaultdict(bool)
que = deque()
# que.append(x)
que.append(0)
isNo = True
while que :
    v = que.popleft()
    visited[v] = True
    # print(v)
    # if v == 1 :
    #     isNo = False
    #     break
    for w in next[v] :
        if w == 1 :
            isNo = False
            break
        # print(visited[w])
        if not(visited[w]) :
            que.append(w)
    if not(isNo) :
        break
print('YNeos'[isNo::2])
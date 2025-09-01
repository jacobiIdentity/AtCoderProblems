#!/usr/bin/env python3
from collections import  defaultdict,deque
n,m = map(int,input().split())
d = defaultdict(set)
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
que = deque()
que.append((0,{0},(0,)))
ans = set()
while que :
    v,visited,path = que.popleft()
    if len(visited)== n :
        ans.add(path)
    for w in d[v] :
        if w in visited :
            continue
        que.append((w,visited|{w},path+(w,)))
print(len(ans))
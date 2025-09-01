#!/usr/bin/env python3
from collections import defaultdict,deque
n,q = map(int,input().split())
d = defaultdict(set)
for _ in range(n-1) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
viisted = [0]*n
que = deque()
que.append(0)
while que :
    v = que.popleft()
    viisted[v] = 1
    for w in d[v] :
        d[w].discard(v)
        que.append(w)
# print(d)
points = [0]*n
for _ in range(q) :
    p,x = map(int,input().split())
    points[p-1] += x
que.append((0,points[0]))
ans = [0]*n
while que :
    v,pt = que.popleft()
    ans[v] = pt
    for w in d[v] :
        que.append((w,pt+points[w]))
print(*ans)


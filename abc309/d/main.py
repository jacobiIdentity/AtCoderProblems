#!/usr/bin/env python3
from collections import defaultdict, deque
n1, n2, m = map(int, input().split())
d = defaultdict(list)
for i in range(m) :
    a, b = map(int, input().split())
    if a == b :
        continue
    d[a].append(b)
    d[b].append(a)
n1Dist, n2Dist = 1, 1
dist = [0]*2+[-1]*(n1+n2+1)
q = deque()
q.append(1)
while q :
    i = q.popleft()
    for j in d[i] :
        if dist[j] == -1 :
            dist[j] = dist[i] + 1
            q.append(j)
# print(n1,dist)
n1Dist = max(dist)
dist = [-1]*(n1+n2)+[0]
q.append(n1+n2)
while q :
    i = q.popleft()
    for j in d[i] :
        if dist[j] == -1 :
            dist[j] = dist[i] + 1
            q.append(j)
# print(n2,dist)
n2Dist = max(dist)
print(n1Dist+n2Dist+1)
# print(n1Dist,n2Dist)
#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
graphSet = defaultdict(set)
Days = defaultdict(int)
for _ in range(m) :
    a,b,d = map(int,input().split())
    if a==b : continue
    a,b = a-1,b-1
    # d = max(Days[(a,b)],d)
    Days[(a,b)] = max(Days[(a,b)],d)
    Days[(b,a)] = max(Days[(a,b)],d)
    graphSet[a].add(b)
    graphSet[b].add(a)
# visited = [0]*n
# que = deque()
# que.append(0)
# while que :
#     v = que.popleft()
#     for w in graphSet[v] :
#         visited[v] = max(Days[(v,w)],visited[v])
#         if visited[w]==0 :
#             que.append(w)
# print(min(visited))
# print(visited)
ans = float('inf')
for i in range(n) :
    tmp = 0
    for j in graphSet[i] :
        tmp = max(tmp,Days[(i,j)])
    ans = min(ans,tmp)
print(ans)
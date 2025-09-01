#!/usr/bin/env python3
from collections import defaultdict,deque
# import heapq
dup = defaultdict(int)
n, m = map(int,input().split())
g = defaultdict(list)
for _ in range(m) :
    a,b = map(int,input().split())
    dup[(a-1,b-1)] += 1
    dup[(b-1,a-1)] += 1
    g[a-1].append(b-1)
    g[b-1].append(a-1)
# visited = [float('inf')]*n
visited = [-1]*n
ans = 0
# que = []
# heapq.heapify(que)
# heapq.heappush(que,(0,0))
visited[0] = 0
# while que :
#     curDist, curNode = heapq.heappop(que)
#     if visited[curNode] < curDist :
#         continue
#     for neighbor in g[curNode] :
#         if visited[neighbor] > curDist+1 :
#             visited[neighbor] = curDist+1
#             heapq.heappush(que,(curDist+1,neighbor))
# if visited[n-1] == float('inf') :
#     print(0)
#     exit()
# ans = 0
# que = deque()
# que.append((n-1,0,1))
# while que :
#     v,stp,weight = que.popleft()
#     if v == 0 :
#         ans += weight
#         continue
#     for w in g[v] :
#         if visited[n-1]-stp-1 == visited[w] :
#             que.append((w,stp+1,weight))
# print(ans%(10**9+7))
cnt = [0]*n
cnt[0] = 1
que = deque()
que.append(0)
while que :
    v = que.popleft()
    for w in g[v] :
        if visited[w] == -1 :
            visited[w] = visited[v]+1
            cnt[w] = cnt[v]
            que.append(w)
        elif visited[w] == visited[v]+1 :
            cnt[w] += cnt[v]
            cnt[w] %= 10**9+7
# print(visited)
# print(cnt)
print(cnt[-1])
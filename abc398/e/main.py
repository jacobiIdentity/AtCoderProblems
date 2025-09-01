#!/usr/bin/env python3
import heapq
from collections import defaultdict,deque
n = int(input())
d = defaultdict(set)
candidates = {(i+1,j+1) for i in range(n) for j in range(i+1,n)}
# print(candidates)
for _ in range(n-1) :
    u,v = map(int,input().split())
    d[u].add(v)
    d[v].add(u)
    candidates.discard((u,v))
# print(candidates)
# print(d)
q = []
heapq.heapify(q)
for u,v in candidates :
    visited = [0]*(n+1)
    visited[u] = 1
    q2 = deque()
    q2.append(u)
    while q2 :
        w = q2.popleft()
        if w ==v :
            break
        for x in d[w] :
            if visited[x]> 0 :
                continue
            visited[x] = visited[w]+1
            q2.append(x)
    # print(visited)
    if visited[v]%2==0 :
        heapq.heappush(q,(u,v))
# print(q)
hand = 'First'
if len(q)%2== 0 :
    hand = 'Second'
print(hand)
if hand == 'First' :
    u,v = heapq.heappop(q)
    print(u,v)
while q :
    u,v = map(int,input().split())
    q.remove((u,v))
    heapq.heapify(q)
    u,v = heapq.heappop(q)
    print(u,v)
    # tmp = []
    # while q :
    #     x,y = heapq.heappop(q)
    #     if x== u and y==v  :
    #         break
    #     tmp.append((x,y))
    # while tmp :
    #     heapq.heappush(q,tmp.pop())
    # heapq.heapify(q)
    # u,v = heapq.heappop(q)


exit()
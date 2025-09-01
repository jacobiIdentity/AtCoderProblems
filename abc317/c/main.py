#!/usr/bin/env python3
# import itertools
from collections import defaultdict,deque
import heapq
n,m = map(int, input().split())
d1 = defaultdict(set)
d2 = defaultdict(int)
for _ in range(m) :
    a, b, c = map(int, input().split())
    d1[a-1].add(b-1)
    d1[b-1].add(a-1)
    d2[(a-1,b-1)] = c
    d2[(b-1,a-1)] = c
print(d1)
print(d2)
ans = 0
for i in range(n) :
    visited = [0]*n
    stack = []
    stack.append((i,0))
    while stack :
        v,cst = stack.pop()
        if visited[v] :
            continue
        ans = max(ans,cst)
        visited[v] = 1
        for w in d1[v] :
            stack.append((w,cst+d2[(v,w)]))


# for grp in itertools.permutations(range(n)) :
#     tmp = 0
#     for i in range(n-1) :
#         if (grp[i],grp[i+1]) not in d2 :
#             break
#         tmp += d2[(grp[i],grp[i+1])]
#     ans = max(ans,tmp)

# for i in range(n) :
#     que = deque()
#     que.append((i,0,{i}))
#     while que :
#         v,cst = que.popleft()
#         ans = max(ans,cst)
#         visited[v]=1
#         for w in d1[v] :
#             if w in path :
#                 continue
#             que.append((w,cst+d2[(v,w)],path|{w}))
print(ans)
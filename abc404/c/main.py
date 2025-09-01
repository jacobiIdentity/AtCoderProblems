#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
if m != n :
    print('No')
    exit()
# uf = UnionFind(n)
d = defaultdict(set)
for _ in range(m) :
    a,b = map(int,input().split())
    d[a-1].add(b-1)
    d[b-1].add(a-1)
    # if uf.same(a-1,b-1) :
        # print('Yes')
        # exit()
    # uf.union(a-1,b-1)
visited = [0]*n
finished = [0]*n
for i in range(n) :
    if visited[i] :
        continue
    stack = []
    stack.append((i,None))
    while stack :
        v,parents = stack.pop()
        if parents is None :
            visited[v] = 1
        else :
            visited[v] = visited[parents]+1
        for w in d[v] :
            if not(visited[w]) :
                stack.append((w,v))
            elif parents==w :
                continue
            else :
                # print(v,w,visited)
                if visited[v] == n :
                    print('Yes')
                else :
                    print('No')
                exit()

print('No')

#!/usr/bin/env python3
from collections import deque
n,q = map(int,input().split())
next = {i:-1 for i in range(1,n+1)}
prev = {i:-1 for i in range(1,n+1)}
for _ in range(q) :
    query = list(map(int,input().split()))
    if query[0] == 1 :
        next[query[1]] = query[2]
        prev[query[2]] = query[1]
    elif query[0] == 2 :
        next[query[1]] = -1
        prev[query[2]] = -1
    else :
        top = query[1]
        q = deque()
        q.append(top)
        while prev[top] != -1 :
            top = prev[top]
            q.appendleft(top)
        top = query[1]
        while next[top] != -1 :
            top = next[top]
            q.append(top)
        print(len(q),*q)
    # print(next)
    # print(prev)
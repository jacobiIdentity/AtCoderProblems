#!/usr/bin/env python3
from collections import deque
t = int(input())
for _ in range(t) :
    n = int(input())
    s = '0'+ input()
    visited = [0]*(2**n)
    que = deque()
    que.append(0)
    visited[0]=1
    while que :
        i = que.popleft()
        for j in range(n) :
            if i&(1<<j) or s[i+(1<<j)]=='1' or visited[i+(1<<j)]:
                continue
            visited[i+(1<<j)] = 1
            que.append(i+(1<<j))
    # print(visited)
    print('YNeos'[1-visited[-1]::2])
            
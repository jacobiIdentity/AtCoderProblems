#!/usr/bin/env python3
from collections import deque
q = int(input())
que = deque()
for _ in range(q) :
    query = input()
    if query[0]=='1' :
        que.append(query[2:])
    else :
        print(que.popleft())

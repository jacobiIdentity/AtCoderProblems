#!/usr/bin/env python3
from collections import deque
n, q = map(int, input().split())
que = deque()
now = 1
for _ in range(q) :
    event = input()
    if event == '1' :
        que.append(now)
        now += 1
    elif event[0] == '2' :
        e, x = map(int, event.split())
        que.remove(x)
    else :
        tmp = que.popleft()
        print(tmp)
        que.append(tmp) 


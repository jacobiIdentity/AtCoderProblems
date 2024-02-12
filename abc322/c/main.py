#!/usr/bin/env python3
from collections import deque
n, m = map(int, input().split())
a_n = deque(list(map(int, input().split())))
i = 1
a = a_n.popleft()
while i < n+1 :
    print(a-i)
    if i == a and i < n :
        a = a_n.popleft()
    i += 1

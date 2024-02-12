#!/usr/bin/env python3
from collections import deque
n = int(input())
s_n = list({input() for _ in range(n)})
ans = set()
for s in s_n :
    if (s not in ans) and (s[::-1] not in ans) :
        ans.add(s)
print(len(ans))
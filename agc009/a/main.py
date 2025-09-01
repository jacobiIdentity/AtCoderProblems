#!/usr/bin/env python3
from collections import deque
n = int(input())
a_n,b_n = [],[]
for _ in range(n) :
    a,b = map(int,input().split())
    a_n.append(a)
    b_n.append(b)
ans = 0
for i in reversed(range(n)):
    ans += (-ans-a_n[i])%b_n[i]
print(ans)
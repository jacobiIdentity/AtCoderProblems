#!/usr/bin/env python3
from collections import defaultdict,deque
h,w = map(int,input().split())
s_h = [input() for _ in range(h)]
ans = 1
quotient = 998244353
tmp = [set() for _ in range(h+w-1)]
for i in range(h) :
    for j in range(w) :
        if s_h[i][j]!= '.' :
            tmp[i+j].add(s_h[i][j])
for i in range(h+w-1) :
    ans *= 2-len(tmp[i])
    ans %= quotient
print(ans%quotient)
#!/usr/bin/env python3
n, m = map(int, input().split())
l, r = -1, n+1
for _ in range(m) :
    l1, r1 = map(int, input().split())
    l = l1 if l < l1 else l
    r = r1 if r > r1 else r
print(max(0, r-l+1))

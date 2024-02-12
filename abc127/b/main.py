#!/usr/bin/env python3
r, d, x0 = map(int, input().split())
for _ in range(10) :
    x0 = x0 * r - d
    print(x0)

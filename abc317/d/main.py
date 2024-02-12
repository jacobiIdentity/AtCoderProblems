#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
tGiseki, zGiseki = 0, 0
x_n, y_n, z_n = [], [], []
sabun = []
for _ in range(n) :
    x, y, z = map(int, input().split())
    zGiseki += z
    if x > y :
        tGiseki += z
    else :
        sabun.append(y-x)
        z_n.append(z)
minGiseki = zGiseki//2 -tGiseki
if minGiseki < 0 :
    print(0)
    exit()

#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
mask1 = 0
for a in a_n :
    mask1 ^= a
print(*[a^mask1 for a in a_n], sep=" ")
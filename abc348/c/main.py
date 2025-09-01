#!/usr/bin/env python3
from collections import defaultdict
n  = int(input())
beans = defaultdict(lambda: float('inf'))
for _ in range(n) :
    a,c = map(int, input().split())
    beans[c] = min(beans[c], a)
print(max(beans.values()))

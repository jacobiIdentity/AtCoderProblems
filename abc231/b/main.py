#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n) :
    d[input()] += 1
print(max([(d[s],s) for s in d])[1])
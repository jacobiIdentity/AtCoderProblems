#!/usr/bin/env python3
from collections import defaultdict,deque
h,w = map(int,input().split())
print(sum([input().count('#') for _ in range(h)]))
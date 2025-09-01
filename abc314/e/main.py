#!/usr/bin/env python3
from collections import deque, defaultdict
import sys
n, m = map(int, input().split())
c_n, p_n, s_ij = [], [], []
for _ in range(n) :
    cps = list(map(int, input().split()))
    c_n.append(cps[0])
    p_n.append(cps[1])
    s_ij.append(sorted(cps[2:]))
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1) :
    

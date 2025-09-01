#!/usr/bin/env python3
from collections import defaultdict,deque
n,m = map(int,input().split())
x_n = sorted(list(set((map(int,input().split())))))
# xUnique = sorted(list(set(x_n)))
x_n.sort()
n = len(x_n)
m = min(m,n)
x_dff = [x_n[i+1]-x_n[i] for i in range(n-1)]
x_dff.sort()
# print(x_dff)
print(sum(x_dff[:n-m]+[0]))

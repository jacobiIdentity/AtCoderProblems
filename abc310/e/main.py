#!/usr/bin/env python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
def f(i,j) :
    if i == j :
        return s[i]
    t = f(i, j-1)
    if t == 1 and s[j] == 1 :
        return 0
    else :
        return 1
        
n = int(input())
s = list(map(int, list(input())))
ans = 0
for i in range(n) :
    for j in range(i,n) :
        ans += f(i,j)
print(ans)
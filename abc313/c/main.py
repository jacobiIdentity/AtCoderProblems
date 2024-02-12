#!/usr/bin/env python3
from collections import defaultdict, deque
import sys
n = int(input())
a_n = sorted(list(map(int, input().split())), reverse=True)
s = sum(a_n)
ave = s//n
rem = s%n
b_n = [ave for _ in range(n)]
for i in range(rem) :
    b_n[i] += 1
ans = 0
for i in range(n) :
    ans += abs(a_n[i]-b_n[i])

print(ans//2)
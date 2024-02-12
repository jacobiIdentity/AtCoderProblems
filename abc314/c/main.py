#!/usr/bin/env python3
from collections import deque, defaultdict
n, m = map(int, input().split())
s = input()
c_n = list(map(int, input().split()))
d1 = defaultdict(list)
for i in range(n) :
    d1[c_n[i]].append(i)
d2 = defaultdict(deque)
for dd1 in d1 :
    t = max(d1[dd1])
    d2[dd1].append(s[t])
    d1[dd1].remove(t)
    for ddd1 in d1[dd1] :
        d2[dd1].append(s[ddd1])
ans = ''
for i in range(n) :
    print(d2[c_n[i]].popleft(),end='')
print('')
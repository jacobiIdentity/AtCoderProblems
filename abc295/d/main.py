#!/usr/bin/env python3
from collections import defaultdict
s = input()
n = len(s)
cSum = [[0]*(n+1) for _ in range(10)]
for i in range(n) :
    sInt = int(s[i])
    for j in range(10) :
        cSum[i][j] = cSum[i-1][j] + 1 if sInt == j else 0


a_n = list(map(int, input().split()))
d = defaultdict(int)
for i in range(n) :
    d[a_n[i]] += 1
ans = 0
for i in d :
    ans += d[i]//2
print(ans)  
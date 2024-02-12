#!/usr/bin/env python3
import itertools
n,m = map(int,input().split())
a_b = [tuple(map(int,input().split())) for _ in range(m)]
k = int(input())
c_d = [tuple(map(int,input().split())) for _ in range(k)]
ans = 0
for d in itertools.product(*c_d) :
    d = set(d)
    tmp = 0
    for a,b in a_b :
        if a in d and b in d :
            tmp += 1
    ans = max(ans, tmp)
print(ans)
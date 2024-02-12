#!/usr/bin/env python3
n,m = map(int,input().split())
a_b = [tuple(map(int,input().split())) for _ in range(m)]
k = int(input())
c_d = [tuple(map(int,input().split())) for _ in range(k)]
ans = 0
for i in range(2**16) :
    d = set()
    for j in range(k) :
        d.add(c_d[j][(i>>j)%2])
    ans = max(ans, sum(a in d and b in d for a,b in a_b ))
print(ans)
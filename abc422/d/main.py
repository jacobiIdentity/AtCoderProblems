#!/usr/bin/env python3
n,k = map(int,input().split())
# q,r = k//(2**n),k%(2**n)
# print(0 if r==0 else 1)
# print(*([q+1]*r+[q]*(2**n-r)))
b_i = [k]
u = 0
for _ in range(n):
    tmp = []
    now = 0
    for x in b_i:
        q, r = x//2,x%2
        tmp.append(q)
        tmp.append(q+r)
        now = max(now, r)
    b_i = tmp
    u = max(u,now)
print(u)
print(*b_i)


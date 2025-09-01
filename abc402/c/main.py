#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
a_ij = [[] for _ in range(m)]
for i in range(m) :
    _,*a_ij[i] = map(int,input().split())
# print(a_ij)
b_n = list(map(int,input().split()))
b_reverse = {b_n[i]-1:i for i in range(n)}
# print(b_n)
# print(b_reverse)
for i in range(m) :
    a_ij[i].sort(key=lambda x:b_reverse[x-1])
# print(a_ij)
ans = [0]*n
for i in range(m) :
    ans[b_reverse[a_ij[i][-1]-1]] += 1
for i in range(1,n) :
    ans[i] += ans[i-1]
print(*ans,sep="\n")
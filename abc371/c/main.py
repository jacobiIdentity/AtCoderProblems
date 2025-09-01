#!/usr/bin/env python3
import itertools
from collections import defaultdict
n = int(input())
mg = int(input())
gG = defaultdict(set)
for _ in range(mg) :
    a,b = map(int,input().split())
    a,b = a-1,b-1
    gG[a].add(b)
    gG[b].add(a)
mh = int(input())
gH = defaultdict(set)
for _ in range(mh) :
    a,b = map(int,input().split())
    a,b = a-1,b-1
    gH[a].add(b)
    gH[b].add(a)
a_ij = [[0]*(i+1)+ list(map(int,input().split())) for i in range(n-1)] + [[0]*(n)]
# print(a_ij)
for i in range(1,n) :
    for j in range(i) :
        a_ij[i][j] = a_ij[j][i]
# print(a_ij)
ans = float('inf')
for ps in itertools.permutations(list(range(n))) :
    # print(type(ps))
    ps = list(ps)
    # print(ps)
    tmp = 0
    for i in range(n-1) :
        for j in range(i+1,n) :
            if (i in gH[j] and ps[i] not in gG[ps[j]]) \
              or (i not in gH[j] and ps[i] in gG[ps[j]]) :
                tmp += a_ij[i][j]
#     if ans >= tmp :
#         print(ps,tmp)
    ans = min(ans,tmp)
#     # print(tmp)
print(ans)
#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
tmp = [list(map(int,input().split())) for _ in range(n)]
# d1 = {i:set(tmp[i][1:]) for i in range(n)}
# a_ij = {i:set(list(map(int,input().split()))[1:]) for i in range(n)}
d1 = defaultdict(set)
d2 = defaultdict(int)
for i in range(n) :
    for j in range(tmp[i][0]) :
        d1[i].add(tmp[i][j+1])
        d2[(i,tmp[i][j+1])] += 1
ans = 0
for i in range(n) :
    for j in range(i+1,n) :
        now = 0
        for x in d1[i]&d1[j] :
            # print(x,d2[(i,x)],d2[(i,j)])
            now += d2[(i,x)]*d2[(j,x)]
        ans = max(ans,now/(tmp[i][0]*tmp[j][0]))
print(ans)
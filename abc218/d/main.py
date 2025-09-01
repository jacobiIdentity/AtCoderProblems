#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
d_x = defaultdict(set)
d_xList = defaultdict(list)
for _ in range(n) :
    x,y = map(int,input().split())
    d_x[x].add(y)
    d_xList[x].append(y)
for x in d_xList :
    d_xList[x].sort()
xKeyList = list(d_x.keys())
xKeyList.sort()
cnt = 0
# ans = set()
for x1i in range(len(xKeyList)) :
    if len(d_x[xKeyList[x1i]]) < 2 :
        continue
    for i in range(len(d_x[xKeyList[x1i]])) :
        for j in range(i+1,len(d_x[xKeyList[x1i]])) :
            for x1j in range(x1i+1,len(xKeyList)) :
                if d_xList[xKeyList[x1i]][i] in d_x[xKeyList[x1j]] and d_xList[xKeyList[x1i]][j] in d_x[xKeyList[x1j]] :
                    cnt += 1
                    # ans.add((xKeyList[x1i],xKeyList[x1j],d_xList[xKeyList[x1i]][i],d_xList[xKeyList[x1i]][j]))
print(cnt)
# print(len(ans))
        
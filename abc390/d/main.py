#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
grp = set()
for i in range(1<<(n*2-1)) :
    strI = format(i, '0'+str(2*n-1)+'b')
    if strI.count('1') != n :
        continue
    tmp = []
    now = 0
    for j in range(2*n-1) :
        if strI[j]== '0' :
            if now > 0 :
                tmp.append(now)
            now = 0
        else :
            now += 1
    if now > 0 :
        tmp.append(now)  
    # tmp.sort()
    if len(tmp) > 1 :
        grp.add(tuple(tmp))
print(grp)
# for g in grp :
ans = {sum(a_n)}
# for g in grp :
    # tmp = []
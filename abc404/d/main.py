#!/usr/bin/env python3
from collections import defaultdict
n,m= map(int,input().split())
c_n= list(map(int,input().split()))
a_ij = [list(map(int,input().split())) for _ in range(m)]
# a_ijSet = [set(a_ij[i][1:]) for i in range(m)]
# print(a_ij)
# print(a_ijSet)
inverseA = defaultdict(set)
ans = float('inf')
for i in range(m) :
    for j in range(1,a_ij[i][0]+1) :
        inverseA[a_ij[i][j]-1].add(i)
# print(inverseA)
for i in range(1,1<<(n*2)) :
    tmpAnimals = set()
    tmpAnimals2 = set()
    tmpCost = 0
    for j in range(n) :
        flg = 1 if i&(1<<j) else 0
        flg += 1 if i&(1<<(j+n)) else 0
        if flg :
            # print(i,j,i&1<<j,i&1<<(j+n))
            tmpCost += c_n[j]*flg
            tmpAnimals2 |= tmpAnimals&inverseA[j]
            tmpAnimals |= inverseA[j]
            if flg ==2 :
                tmpAnimals2 |= inverseA[j]
    # print(bin(i), tmpCost,tmpAnimals)
    if len(tmpAnimals)== m and len(tmpAnimals2)==m:
        ans = min(ans,tmpCost)
print(ans)
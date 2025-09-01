#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
primes = []
thievs = set()
maxA = max(a_n)
for tmp in range(2,maxA+1)  :
    if tmp not in thievs :
        primes.append(tmp)
        for mltpl in range(tmp,(maxA//tmp)*tmp+1,tmp) :
            thievs.add(mltpl)
# print(thievs)
# print(primes)
d = defaultdict(set)
for i in range(n) :
    for p in primes :
        if a_n[i]%p == 0 :
            d[p].add(i)
# print(d)
ans = float('inf')
for biI in range(2<<len(primes)) :
    tmpSet = set()
    tmpNum = 1
    for masks in range(len(primes)) :
        if biI&(2<<masks) :
            tmpSet |= d[primes[masks]]
            tmpNum *= primes[masks]
    # print(biI,len(tmpSet),tmpSet,tmpNum)
    if len(tmpSet) == n :
        ans = min(ans,tmpNum)
print(ans)




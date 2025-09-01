#!/usr/bin/env python3
import itertools,bisect
n,q = map(int,input().split())
a_i = list(map(int,input().split()))
a_i.sort()
aMax = a_i[-1]
acs = list(itertools.accumulate([0]+a_i))
# print(a_i)
# print(acs)
for _ in range(q):
    b = int(input())
    if b > aMax :
        print(-1)
    # elif b == aMax :
    #     print(acs[-1])
    else :
        pos = bisect.bisect_left(a_i,b)
        print(acs[pos] +(b-1)*(n-pos)+1)

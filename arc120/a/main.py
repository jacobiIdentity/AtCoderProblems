#!/usr/bin/env python3
from collections import defaultdict,deque
n = int(input())
a_n = list(map(int,input().split()))
maxA = 0
acs = [a_n[i] for i in range(n)]
for i in range(1,n) :
    acs[i] += acs[i-1]
# print(acs)
for i in range(1,n) :
    acs[i] += acs[i-1]
# print(acs)
for i in range(n) :
    maxA = max(maxA,a_n[i])
    print(maxA*(i+1)+acs[i])
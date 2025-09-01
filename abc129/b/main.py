#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
acs = [0]+list(itertools.accumulate(a_n))
ans = float('inf')
for i in range(1,n+1) :
    ans = min(ans,abs(acs[i]-(acs[n]-acs[i])))
print(ans)
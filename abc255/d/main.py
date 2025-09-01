#!/usr/bin/env python3
import bisect
import itertools
n,q = map(int,input().split())
a_n = list(map(int,input().split()))
a_n.sort()
acs = [0]+list(itertools.accumulate(a_n))
for _ in range(q) :
    x = int(input())
    pos = bisect.bisect_left(a_n,x)
    print(x*(pos*2-n)+acs[n]-2*acs[pos])
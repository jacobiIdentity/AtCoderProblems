#!/usr/bin/env python3
import bisect
import itertools
n,q = map(int, input().split())
r_i = sorted(list(map(int, input().split())))
cms = list(itertools.accumulate(r_i))
for _ in range(q) :
    print(bisect.bisect_right(cms,int(input()))) 
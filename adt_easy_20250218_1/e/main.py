#!/usr/bin/env python3
import itertools
n,m = map(int,input().split())
s_n = [input() for _ in range(n)]
isYes = False
for p in itertools.permutations(s_n) :
    t_n = list(p)
    # print(t_n)
    for i in range(n-1) :
        isAlmostEquali = True
        d = 0
        for k in range(m) :
            if t_n[i][k] != t_n[i+1][k] :
                d += 1
        if d != 1 :
            isAlmostEquali = False
            break
    isYes = isAlmostEquali
    if isYes : break
print('YNeos'[not(isYes)::2])
#!/usr/bin/env python3
import itertools
from collections import defaultdict
h, w = map(int, input().split())
c_hw = [list(input()) for _ in range(h)]
isEnd = False
while not(isEnd) :
    cs = set()
    for i in range(h) :
        c_h_ = set(c_hw[i])
        if len(c_h_) == 1  or (len(c_h_) == 2 and '.' in c_h_ ):
            cs.add((i,'r'))
    for j in range(w) :
        c__w = {c_hw[i][j] for i in range(h)}
        if len(c__w) == 1  or (len(c__w) == 2 and '.' in c__w ):
            cs.add((i,'c'))
    if len(cs) == 0 :
        isEnd = True
        break
    for k,d in cs :
        if d == 'r' :
            for j in range(w) :
                c_hw[k][j] = '.'
        else :
            for i in range(h) :
                c_hw[i][k] = '.'
ans = list(itertools.chain.from_iterable(c_hw))
print(len(ans)-ans.count('.'))
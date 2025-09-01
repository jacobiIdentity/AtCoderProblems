#!/usr/bin/env python3
import itertools
n = input()
ans = 0
for i in range(1,1<<len(n)-1) :
    a,b = [],[]
    for j in range(len(n)) :
        if i&(1<<j) :
            a.append(n[j])
        else :
            b.append(n[j])
    for aList in itertools.permutations(a) :
        aN = int(''.join(aList))
        if len(str(aN)) < len(a) :
            continue
        for bList in itertools.permutations(b) :
            bN = int(''.join(bList))
            if len(str(bN)) < len(b) :
                continue
            ans = max(ans,aN*bN)
print(ans)

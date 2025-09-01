#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
ans = list(itertools.accumulate(a_n,lambda x,y:x^y))[-1]
for i in range(1,n) :
    for splits in itertools.combinations(range(1,n),i) :
        splits = [0]+list(splits)+[n]
        xors = 0
        for j in range(i+1) :
            ors = 0
            for k in range(splits[j],splits[j+1]) :
                ors |= a_n[k]
            xors ^= ors
        ans = min(ans,xors)



print(ans)

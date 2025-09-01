#!/usr/bin/env python3
import itertools,functools
n,k = map(int,input().split())
s = list(input())
ans = set()
for t in itertools.permutations(s) :
    isP = True
    for i in range(n-k+1) :
        for j in range(k) :
            if t[i+j] != t[i+k-j-1] :
                isP = False
                break
        if isP : break
    if isP : continue
    ans.add("".join(t))
print(len(ans))
print(ans)

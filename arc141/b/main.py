#!/usr/bin/env python3
import bisect
t = int(input())
for _ in range(t) :
    n = input()
# for i in range(11,1000+1) :
    # n = str(i)
    candidates = set()
    if len(n) > 2 :
        candidates.add(int('9'*(len(n)-1)))
    for i in range(1,10) :
        # print(n,len(n))
        if len(n)%i == 0 and len(n)>i :
            candidates.add(int(n[:i]*(len(n)//i)))
            if int(n[:i])-1 >= 10**(i-1) :
                candidates.add(int(str(int(n[:i])-1)*(len(n)//i)))
    candidates = list(candidates)
    candidates.sort()
    candidates.reverse()
    # print(candidates)
    for c in candidates :
        if int(n) >= c :
            print(c)
            # print(n,c)
            break

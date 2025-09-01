#!/usr/bin/env python3
n = int(input())
s = input()
rSet,gSet,bSet = set(),set(),set()
for i in range(n) :
    if s[i] == 'R' : rSet.add(i)
    if s[i] == 'G' : gSet.add(i)
    if s[i] == 'B' : bSet.add(i)
ans = len(rSet)*len(gSet)*len(bSet)
for r in rSet :
    for g in gSet :
        # p,q = min(r,g), max(r,g)
        p,q = r,g
        if p > q :
            p,q = q,p
        if (q-p)%2 == 0 and (p+q)//2 in bSet :
            ans -= 1
        if 2*p-q in bSet :
            ans -= 1
        if 2*q-p in bSet :
            ans -= 1
print(ans)

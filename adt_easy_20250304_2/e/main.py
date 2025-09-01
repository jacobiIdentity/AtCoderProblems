#!/usr/bin/env python3
import math
s = input()
d = {chr(ord('a')+i):0 for i in range(26)}
for ss in s :
    d[ss] += 1
ans = (len(s)*(len(s)-1))//2
sub = 0
for a in d :
    if d[a] > 1 :
        sub += math.comb(d[a],2)
if sub > 0 : sub -= 1
print(ans-sub)
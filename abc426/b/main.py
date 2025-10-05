#!/usr/bin/env python3
s = list(input())
d = {}
for ss in s :
    if ss not in d :
        d[ss] = 1
    else :
        d[ss] += 1
for dd in d :
    if d[dd] == 1:
        print(dd)
        exit()
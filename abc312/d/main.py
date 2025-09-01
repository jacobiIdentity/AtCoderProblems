#!/usr/bin/env python3
s = input()
l = len(s)
ls = s.count('(')
rs = s.count(')')
qs = s.count('?')
dp = [[0]*(l+1) for _ in range(2)]
for i in range(l+1) :
    for j in range(l+1) :
        
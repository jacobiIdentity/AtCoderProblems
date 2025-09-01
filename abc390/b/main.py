#!/usr/bin/env python3
from fractions import Fraction
n = int(input())
a_n = list(map(int,input().split()))
isYes = True
r = Fraction(a_n[1],a_n[0])
for i in range(n-1) :
    if Fraction(a_n[i+1],a_n[i]) != r :
        isYes = False
print('YNeos'[not(isYes)::2])

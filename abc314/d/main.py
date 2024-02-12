#!/usr/bin/env python3
from collections import deque, defaultdict
import sys
n = int(input())
s = list(input())
q = int(input())
isSmall = False
isLarge = False
special = []
for _ in range(q) :
    t, x, c = input().split()
    if t == '1' :
        s[int(x)-1] = c
        special.append(int(x)-1)
    elif t == '2' :
        isSmall, isLarge = True, False
        special.clear()
    else :
        isSmall, isLarge = False, True
        special.clear()
for i in range(n) :
    if not(isSmall) and not(isLarge) :
        print(*s, sep='')
        exit()
    if isSmall and i not in special :
        print(s[i].lower(),end='')
    elif isLarge and i not in special :
        print(s[i].upper(),end='')
    else :
        print(s[i],end='')
print('')
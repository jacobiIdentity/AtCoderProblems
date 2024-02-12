#!/usr/bin/env python3
n = int(input())
s_n = [input() for _ in range(n)]
isYes = False
for s1 in s_n :
    for s2 in s_n :
        if s1 == s2 :
            continue
        if s1+s2 == (s1+s2)[::-1] :
            isYes = True
print('Yes' if isYes else 'No')
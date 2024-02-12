#!/usr/bin/env python3
import sys
l, r  = map(int, input().split())
if r - l >= 673 :
    print(0)
    exit()
l, r = l%2019, r%2019
if l > r or l == 0 or r == 0 :
    print(0)
    exit()
if (l%673 == 0 or r%673 == 0) and (r-l > 2 or (r-l == 1 and (r%3 == 0 or l%3 == 0 or (l+1)%3 == 0))) :
    print(0)
    exit()
ans = 2020
for i in range(l, r+1) :
    for j in range(i+1, r+1) :
        ans = min(ans, (i*j)%2019)
print(ans)

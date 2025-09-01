#!/usr/bin/env python3
import bisect
k = int(input())
ans = []
d = 0
while k >= 1<<d :
    if k&(1<<d) :
        ans.append('2')
    else :
        ans.append('0')
    d+=1
print(''.join(reversed(ans)))
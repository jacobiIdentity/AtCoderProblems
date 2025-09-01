#!/usr/bin/env python3
import bisect
n = int(input())
a_n = list(map(int,input().split()))
ans = 0
for a in a_n :
    pos =  bisect.bisect_left(a_n,2*a)
    ans += n-pos
print(ans)

#!/usr/bin/env python3
import bisect
n, m = map(int, input().split())
a_n = sorted(list(map(int, input().split())))
b_m = sorted(list(map(int, input().split())))
l = 0
r = max(a_n[-1],b_m[-1])+1
x =0
while (r-l)>1 :
    x = (l+r)//2
    posXa = bisect.bisect_right(a_n,x)
    posXb = bisect.bisect_left(b_m,x)
    if posXa >= m-posXb :
        r = x
    else :
        l = x
if bisect.bisect_right(a_n,x) < m - bisect.bisect_left(b_m,x) :
    x =r
print(x)

# print(l,r)

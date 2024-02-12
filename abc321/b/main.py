#!/usr/bin/env python3
n, x = map(int, input().split())
a_n = sorted(list(map(int, input().split())))
if sum(a_n) -a_n[-1] >= x :
    print(0)
elif  sum(a_n) -a_n[0] < x :
    print(-1)
else :
    print(x -sum(a_n)+a_n[0]+a_n[-1])
#!/usr/bin/env python3
n, k = map(int, input().split())
a_n = sorted(list(map(int, input().split())))
s = set([a_n[0]*i for i in range(k+1)])
for i in range(1,n) :
    m = max(s)
    tmp = 


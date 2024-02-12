#!/usr/bin/env python3
a, m, l, r = map(int, input().split())
rPrime = (r-a)//m
lPrime = (l-a)//m
print(rPrime-lPrime + (1 if (l-a)%m == 0 else 0))


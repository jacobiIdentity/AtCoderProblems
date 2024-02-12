#!/usr/bin/env python3
import sys
n, m = map(int, input().split())
if n*n < m :
    print(-1)
    exit()
if m <= n :
    print(m)
    exit()
if m%n == 0 :
    print(m)
    exit()
for i in range(m, n*n+1) :
    for j in range(n//m+1, n+1) :
        if i%j == 0 and i//j < n+1 :
            print(i)
            exit()
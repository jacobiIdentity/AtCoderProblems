#!/usr/bin/env python3
q = int(input())
a = []
for _ in range(q) :
    n, xk = map(int, input().split())
    if n == 1 :
        a.append(xk)
    else :
        print(a[-xk])
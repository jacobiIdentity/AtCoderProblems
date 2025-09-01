#!/usr/bin/env python3
n = int(input())
a_n = [int(input()) for _ in range(n)]
b_n = sorted(a_n)
for i in range(n) :
    if a_n[i]!= b_n[-1] :
        print(b_n[-1])
    else :
        print(b_n[-2])
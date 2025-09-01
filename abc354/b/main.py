#!/usr/bin/env python3
n = int(input())
s_n, sumC = [], 0
for _ in range(n) :
    s, c = input().split()
    s_n.append(s)
    sumC += int(c)
print(sorted(s_n)[sumC%n])
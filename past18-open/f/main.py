#!/usr/bin/env python3
s = input()
n = int(input())
d = dict()
for _ in range(n) :
    c,v = input().split()
    d[c] = int(v)
print(eval(s,d))
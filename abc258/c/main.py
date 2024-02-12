#!/usr/bin/env python3
n,q = map(int, input().split())
s = input()
p = 0
for _ in range(q) :
    t, x = map(int, input().split())
    if t == 1 :
        p += x
        p %= n
    else :
        # print(p,x)
        print(s[(-p+x-1)%n])
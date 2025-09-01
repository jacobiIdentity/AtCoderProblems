#!/usr/bin/env python3
n = int(input())
a = 2
oks=set()
while a**2 <= n :
    b = 2
    while a**b <= n :
        oks.add(a**b)
        b+=1
    a+=1
print(n-len(oks))
#!/usr/bin/env python3
n = int(input())
digits = []
t = n
while t > 0 :
    digits.append(n%10)
    n //= 10
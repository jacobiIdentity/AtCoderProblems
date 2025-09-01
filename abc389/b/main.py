#!/usr/bin/env python3
x = int(input())
n = 1
while x != 1 :
    n += 1
    x //= n
print(n)
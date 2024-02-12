#!/usr/bin/env python3
import sys
a, b, c, d = map(int, input().split())
if c > d :
    c, d = d, c
abcCnt = b//c - (a-1)//c
abdCnt = b//d - (a-1)//d
if c == d :
    print(b-a+1-abcCnt)
    exit()
x, y, g = c, d, 0
while x > 0 :
    x, y = y%x, x
g = c*d//y
abgCnt = b//g - (a-1)//g
print(b-a+1-abcCnt-abdCnt+abgCnt)
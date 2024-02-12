#!/usr/bin/env python3
import sys
n = int(input())
s = input()
a, b, c = False, False, False
for i in range(n) :
    if s[i] == 'A' :
        a = True
    elif s[i] == 'B' :
        b = True
    elif s[i] == 'C' :
        c = True
    if a and b and c :
        print(i+1)
        exit()


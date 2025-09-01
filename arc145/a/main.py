#!/usr/bin/env python3
n = int(input())
s = input()
if n == 2 :
    if s == 'AB' or s == 'BA' : print('No')
    else :print('Yes')
    exit()
if s[0] == 'A' and s[-1] == 'B' : print('No')
else :print('Yes')

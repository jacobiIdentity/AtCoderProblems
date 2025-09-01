#!/usr/bin/env python3
n = int(input())
s = input()
print('YNeos'[not(s.count('o')>=1 and s.count('x')==0)::2])
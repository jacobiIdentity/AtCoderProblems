#!/usr/bin/env python3
n = int(input())
n = int(n*1.08)
print('Yay!' if n<206 else ('so-so' if n==206 else ':('))
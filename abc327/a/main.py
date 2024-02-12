#!/usr/bin/env python3
n = int(input())
s = input()
print('Yes' if s.find('ab') != -1 or s.find('ba') != -1 else 'No')
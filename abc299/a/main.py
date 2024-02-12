#!/usr/bin/env python3
n = int(input())
s = input()
v1 = s.find('|')
v2 = s.find('|', s.find('|')+1)
a = s.find('*')
print('in' if  v1 < a and a < v2 else 'out')
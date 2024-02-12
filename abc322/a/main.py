#!/usr/bin/env python3
n = int(input())
s = input()
print(s.find('ABC')+1 if s.find('ABC') != -1 else -1)
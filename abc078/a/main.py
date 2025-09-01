#!/usr/bin/env python3
x,y = input().split()
print('<' if ord(x) < ord(y) else ('=' if x==y else '>'))
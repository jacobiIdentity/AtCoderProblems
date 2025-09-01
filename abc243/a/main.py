#!/usr/bin/env python3
v,a,b,c = map(int,input().split())
print('F' if v%(a+b+c)<a else ('M' if v%(a+b+c) < a+b else 'T'))
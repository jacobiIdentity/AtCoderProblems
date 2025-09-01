#!/usr/bin/env python3
x,y = map(int,input().split())
print('<' if x < y else ('=' if x==y else '>'))
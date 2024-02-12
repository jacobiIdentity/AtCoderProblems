#!/usr/bin/env python3
n,s,d = map(int,input().split())
isYes = False
for _ in range(n) :
    x, y = map(int,input().split())
    if x < s and y > d :
        isYes = True
print('Yes' if isYes else 'No')

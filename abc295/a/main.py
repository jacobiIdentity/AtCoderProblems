#!/usr/bin/env python3
a = ['and', 'not', 'that', 'the', 'you']
n = input()
w_n = list(input().split())
isYes = False
for w in w_n :
    if w in a :
        isYes = True
print('Yes' if isYes else 'No')
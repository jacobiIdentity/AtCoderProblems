#!/usr/bin/env python3
import sys
s = input()
if len(s) == 1 :
    print('Yes' if int(s) % 8 == 0 else 'No')
    exit()
if len(s) == 2 :
    print('Yes' if int(s) % 8 == 0 or int(s[1]+s[0]) % 8 == 0 else 'No')
    exit()
d8 = {}
for i in range(102//8, 1000//8) :
    tmp = str(i*8)
    if '0' in tmp :
        continue
    d8[i*8] = [0]*9
    for j in range(len(tmp)) :
        d8[i*8][int(tmp[j])-1] += 1
digits = [0]*9
for i in range(len(s)) :
    digits[int(s[i])-1] += 1
for i in d8 :
    isYes = True
    for j in range(9) :
        if digits[j] < d8[i][j] :
            isYes = False
            break
    if isYes :
        print('Yes')
        exit()
print('No')

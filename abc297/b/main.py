#!/usr/bin/env python3
import sys
s = input()
b1, b2, r1, k, r2 = -1, -1, -1, -1, -1
for i in range(8) :
    if s[i] == 'B' :
        if b1 == -1 :
            b1 = i
            continue
        elif (b1-i)%2 == 0 :
            print('No')
            exit()
    elif s[i] == 'K' :
        if r1 == -1 :
            print('No')
            exit()
        elif r2 != -1 :
            print('No')
            exit()
        else :
            k = i
    elif s[i] == 'R' :
        if r1 == -1 :
            r1 = i
        else :
            r2 = i
print('Yes')

        
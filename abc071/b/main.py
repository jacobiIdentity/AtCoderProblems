#!/usr/bin/env python3
import sys
s = input()
a = [True]*26
for ss in s :
    a[ord(ss)-ord('a')] = False
for i in range(26) :
    if a[i] :
        print(chr(i+ord('a')))
        exit()
print('None')

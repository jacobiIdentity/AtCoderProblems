#!/usr/bin/env python3
s = input()
ans = 'z'
for i in range(26) :
    if chr(ord('a')+i) not in s :
        print(chr(ord('a')+i))
        exit()

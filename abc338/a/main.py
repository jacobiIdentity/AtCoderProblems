#!/usr/bin/env python3
s = input()
isYes = s[0].isupper()
for i in range(1,len(s)) :
    if s[i].isupper() :
        isYes = False
print('Yes' if isYes else 'No')
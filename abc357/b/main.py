#!/usr/bin/env python3
s = input()
# if len(set(s)&set('ABCDEFFGHIJKLMNOPQRSTUVWXYZ')) > len(set(s)&set('ABCDEFFGHIJKLMNOPQRSTUVWXYZ'.lower())) :
#     print(s.upper())
# else :
#     print(s.lower())
isLs = 0
for i in range(len(s)):
    if s[i].islower() :
        isLs += 1
if isLs < len(s) - isLs :
    s = s.upper()
else :
    s = s.lower()
print(s)


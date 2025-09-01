#!/usr/bin/env python3
s = input()
subStrings = set()
for i in range(len(s)) :
    for j in range(i,len(s)+1) :
        if s[i:j] != '' :
            subStrings.add(s[i:j]) 
print(len(subStrings))
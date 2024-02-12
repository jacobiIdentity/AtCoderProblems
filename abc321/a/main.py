#!/usr/bin/env python3
s = input()
for i in range(len(s)-1) :
    if int(s[i]) <= int(s[i+1]) :
        print('No')
        exit()
print('Yes')

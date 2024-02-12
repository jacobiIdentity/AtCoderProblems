#!/usr/bin/env python3
s = input()
for i in range(8) :
    if s[2*i+1] == '1' :
        print('No')
        exit()
print('Yes')

#!/usr/bin/env python3
import sys
s = input()
for i in range(len(s)) :
    if s[i].isupper() :
        print(i+1)
        exit()
#!/usr/bin/env python3
s = input()+"X"
t = input()
for i in range(len(s)) :
    if s[i]!=t[i] :
        print(i+1)
        exit()
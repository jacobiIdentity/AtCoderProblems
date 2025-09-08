#!/usr/bin/env python3

s=input()
if s[-1]=="8" :
    print(str(int(s[0])+1)+"-1")
else :
    print(s[0:2]+str(int(s[-1])+1))

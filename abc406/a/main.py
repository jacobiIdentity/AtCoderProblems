#!/usr/bin/env python3
a,b,c,d = map(int,input().split())
isNo = True
if c < a :
    isNo = False
elif a==c and d < b :
    isNo = False
print('YNeos'[isNo::2])
#!/usr/bin/env python3
r,x = map(int,input().split())
isNo = False
if x == 1 and not(1600<=r<3000) :
    isNo = True
if x == 2 and not(1200<=r<2400) :
    isNo = True
print('YNeos'[isNo::2])

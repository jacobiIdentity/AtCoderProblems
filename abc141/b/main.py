#!/usr/bin/env python3
s = input()
isNo = False
for i in range(len(s)) :
    if s[i]=="L" and i%2==0 :
        isNo = True
    if s[i]=="R" and i%2==1 :
        isNo = True
print('YNeos'[isNo::2])
    
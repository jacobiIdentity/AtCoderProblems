#!/usr/bin/env python3
s = input()
t = input()
sTmp, tTmp = 0, 0
while sTmp < len(s) :
    if s[sTmp] == t[tTmp] :
        if sTmp == len(s)-1 :
            print(tTmp+1)
        else :
            print(tTmp+1, end=" ")
        sTmp += 1
        tTmp += 1
    else :
        tTmp += 1

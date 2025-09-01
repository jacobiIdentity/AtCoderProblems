#!/usr/bin/env python3
s = input()
t = input()
isNo = False
for i in range(1,len(s)) :
    if s[i].isupper()  :
        isIn = False
        for j in range(len(t)) :
            if s[i-1]==t[j] :
                isIn = True
                break
        if not isIn :
            isNo = True
print('YNeos'[isNo::2])

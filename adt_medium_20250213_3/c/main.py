#!/usr/bin/env python3
s,t= input().split()
isY = False
for w in range(1,len(s)-1) :
    for c in range(1,w+1) :
        tmp = ''
        for i in range(len(s)//w) :
            if w*i+c-1<len(s) :
                tmp += s[w*i+c-1]
        if tmp == t :
            isY = True
            break
    if isY : break
print('YNeos'[not(isY)::2])
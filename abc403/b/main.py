#!/usr/bin/env python3
t = input()
u = input()
isNo = True
for i in range(len(t)-len(u)+1) :
    isYes = True
    for j in range(len(u)) :
        if t[i+j]!='?' and t[i+j]!=u[j] :
            isYes = False
            break
    if isYes :
        isNo = False
print('YNeos'[isNo::2])
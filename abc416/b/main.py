#!/usr/bin/env python3
s = input()
t = []
i = 0
isOK = True
while i<len(s) :
    if isOK and s[i]=='.' :
        t.append('o')
        isOK = False
    elif not(isOK) and s[i]=='#' :
        isOK = True
        t.append(s[i])
    else :
        t.append(s[i])
    i+=1
print(''.join(t))
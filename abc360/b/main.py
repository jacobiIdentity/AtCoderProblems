#!/usr/bin/env python3
s, t = input().split()
for w in range(1,len(s)) :
    for c in range(1,w+1 ) :
        i = 0
        tmp = ""
        while i+c-1<len(s) :
            tmp += s[i+c-1]
            i += w
        if tmp == t :
            print('Yes')
            exit()
print('No')

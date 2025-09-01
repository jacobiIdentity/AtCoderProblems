#!/usr/bin/env python3
s = input()
if s.count(s[0]) == 1 :
    print(1)
else :
    for i in range(len(s)) :
        if s[i] != s[0] :
            print(i+1)

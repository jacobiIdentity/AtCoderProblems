#!/usr/bin/env python3
n = int(input())
s = input()
if n == 1:
    print('Yes')
else :
    flg = True
    for i in range(1,n) :
        if s[i] == s[i-1] :
            flg = False
    print('Yes' if flg else 'No')

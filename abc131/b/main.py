#!/usr/bin/env python3
import sys
n, l = map(int, input().split())
al = n*(l+l+n-1)//2
if l > -1 :
    print(al-l)
else :
    tmp = l
    for _ in range(1,n) :
        tmp += 1
        if tmp > -1 :
            break
    print(al-tmp)
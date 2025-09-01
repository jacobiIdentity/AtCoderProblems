#!/usr/bin/env python3
n,l,r = map(int,input().split())
for i in range(n) :
    tmp = i+1
    if l <= i+1 <= r :
        tmp = r + l - i-1
    if i != n-1 :
        print(tmp, end=" ")
    else :
        print(tmp)
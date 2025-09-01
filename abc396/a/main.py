#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
isNo = True
for i in range(n-2) :
    if a_n[i]==a_n[i+1]==a_n[i+2] :
        isNo = False
print('YNeos'[isNo::2])
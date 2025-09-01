#!/usr/bin/env python3
n = int(input())
a_n= list(map(int,input().split()))
isN = False
for i in range(n-1) :
    if a_n[i] >= a_n[i+1] :
        isN = True
print('YNeos'[isN::2])
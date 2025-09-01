#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
c_nm = list(sorted(a_n+b_n))
isYes = False
for i in range(n+m-1) :
    if c_nm[i] in a_n and c_nm[i+1] in a_n :
        isYes = True
        break
print('YNeos'[not(isYes)::2])
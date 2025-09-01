#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
b_m = list(map(int,input().split()))
c_nm = sorted(a_n+b_m)
isANow = True
for i in range(n+m) :
    if i == 0 :
        isANow = True  if c_nm[i] in a_n else False
    else :
        if isANow and c_nm[i] in a_n :
            print('Yes')
            exit()
        elif c_nm[i] in a_n :
            isANow = True
        else :
            isANow = False
print('No')

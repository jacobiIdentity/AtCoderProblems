#!/usr/bin/env python3
n,m =map(int,input().split())
ns = [0]*n
for _ in range(m) :
    a,b = input().split()
    if b == 'M' :
        ns[int(a)-1] += 1
    if b == 'M' and ns[int(a)-1] == 1 :
        print('Yes')
    else :
        print('No')


#!/usr/bin/env python3
n,a,b = map(int,input().split())
for i in range(a*n) :
    tmp = []
    for j in range(b*n) :
        tmp.append('.' if (i//a+j//b)%2 == 0 else '#')
    print(''.join(tmp))
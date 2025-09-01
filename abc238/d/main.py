#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    a,s = map(int,input().split())
    print('Yes' if s-2*a>=0 and (s-2*a)&a==0 else 'No')
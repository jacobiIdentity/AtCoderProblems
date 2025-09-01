#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    l,r = map(int,input().split())
    if r < 2*l :
        print(0)
    else :
        print(((r-2*l+1)*(r-2*l+2))//2)

#!/usr/bin/env python3
n,k,q = map(int,input().split())
cnts = [k-q]*n
for i in range(q) :
    cnts[int(input())-1] += 1
for i in range(n) :
    print('YNeos'[(cnts[i]<1)::2])
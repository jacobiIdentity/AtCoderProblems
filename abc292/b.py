#!/usr/bin/env python3
n, q = map(int,input().split())
ps = [0]*n
for _ in range(q) :
    i, x = map(int,input().split())
    if i == 1 :
        ps[x-1] += 1
    elif i == 2 :
        ps[x-1] = 2
    else :
        print('Yes' if ps[x-1] > 1 else 'No')

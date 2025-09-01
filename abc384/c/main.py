#!/usr/bin/env python3
a,b,c,d,e = map(int,input().split())
ans = []
for i in range(1,32) :
    k = ''
    v = 0
    if i & (1<<4) : 
        k +='A'
        v += a
    if i & (1<<3) : 
        k +='B'
        v += b
    if i & (1<<2) : 
        k +='C'
        v += c
    if i & (1<<1) : 
        k +='D'
        v += d
    if i & (1<<0) : 
        k +='E'
        v += e
    ans.append((v,k))
ans.sort(key= lambda x: (-x[0],x[1]))
for v,k in ans :
    print(k)
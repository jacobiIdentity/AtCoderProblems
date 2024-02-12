#!/usr/bin/env python3
n,k = map(int, input().split())
a_k = sorted(list(map(int, input().split())))
if k%2 == 0 :
    print(sum([a_k[2*i+1]-a_k[2*i] for i in range(k//2)]))
else :
    diff = [0]+[a_k[i+1]-a_k[i] for i in range(k-1)]+[0]
    tmp,maxA = 0, 0
    for i in range(k) :
        if tmp <= diff[i] :
            tmp = diff[i]
            maxA = i
    a_k.pop(maxA)
    print(sum([a_k[2*i+1]-a_k[2*i] for i in range(k//2)]))
#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
k,t  = 0, 0
for i in range(2,max(a_n)+1) :
    tmp = 0
    for a in a_n :
        tmp += 1 if a%i == 0 else 0
    if t < tmp :
        k,t = i,tmp

print(k)
#!/usr/bin/env python3
n = int(input())
s_n = list(map(int, input().split()))
asp = set()

for i in range(1,1000) :
    for j in range(1,1000) :
        t = 4*i*j+3*i+3*j
        if t < 1001 :
            asp.add(4*i*j+3*i+3*j)
        else :
            break
    if 4*i*1+3*i+3 > 1000 :
        break
print(len(list(filter(lambda x: x not in asp, s_n))))

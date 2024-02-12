#!/usr/bin/env python3
import sys
n = int(input())
a_n = list(map(int, input().split()))
d = [0]*9
for i in a_n :
    if i < 400 :
        d[0] = 1
    elif i < 800 :
        d[1] = 1
    elif i < 1200 :
        d[2] = 1
    elif i < 1600 :
        d[3] = 1
    elif i < 2000 :
        d[4] = 1
    elif i < 2400 :
        d[5] = 1
    elif i < 2800 :
        d[6] = 1
    elif i < 3200 :
        d[7] = 1
    else :
        d[8] += 1
if sum(d) == d[8] :
    print(1, d[8])
    exit()
print(sum(d)-d[8], sum(d))
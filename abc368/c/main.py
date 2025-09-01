#!/usr/bin/env python3
n = int(input())
h_n = list(map(int,input().split()))
t = 0
for i in range(n) :
    tmp = (h_n[i]//5)*3
    if t%3 == 0 :
        if h_n[i]%5 == 1 :
            tmp += 1
        elif h_n[i]%5 == 2 :
            tmp += 2
        elif h_n[i]%5 != 0 :
            tmp += 3
    elif t%3 == 1 :
        if h_n[i]%5 == 1 :
            tmp += 1
        elif h_n[i]%5 != 0 :
            tmp += 2
    else :
        if h_n[i]%5 == 4 :
            tmp += 2
        elif h_n[i]%5 != 0 :
            tmp += 1
    t += tmp
print(t)

#!/usr/bin/env python3
n,m = map(int,input().split())
h_n = list(map(int,input().split()))
for i in range(n) :
    if m >= h_n[i] :
        m -= h_n[i]
    else :
        print(i)
        exit()
print(n)
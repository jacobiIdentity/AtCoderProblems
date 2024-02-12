#!/usr/bin/env python3
n, h, x = map(int, input().split())
p_n = list(map(int, input().split())) 
for i in range(n) :
    if p_n[i] + h >= x :
        print(i+1)
        exit()

#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
for i in range(n-1) :
    s,t = map(int,input().split())
    a_n[i+1] += t*(a_n[i]//s)
print(a_n[-1])
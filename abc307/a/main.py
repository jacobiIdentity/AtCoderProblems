#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
for i in range(n) :
    
    print(sum(a_n[i*7:(i+1)*7]), end=(" " if i != n-1 else "\n"))
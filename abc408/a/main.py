#!/usr/bin/env python3
n,s = map(int,input().split())
t_n = [0]+list(map(int,input().split()))
for i in range(n) :
    if t_n[i+1]-t_n[i]>s :
        print('No')
        exit()
print('Yes')
    
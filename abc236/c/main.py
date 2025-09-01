#!/usr/bin/env python3
n,m = map(int,input().split())
s_n = input().split()
t_m = set(input().split())
for s in s_n :    
    print('YNeos'[not(s in t_m)::2])
#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(lambda x:x//k,filter(lambda x:x%k==0,map(int,input().split()))))
print(*a_n)
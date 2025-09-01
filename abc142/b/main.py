#!/usr/bin/env python3
n,k = map(int,input().split())
h_n = list(map(int,input().split()))
print(len(list(filter(lambda x:x >=k,h_n))))
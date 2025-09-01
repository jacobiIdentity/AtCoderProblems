#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = set(map(int,input().split()))
b_m = set(map(int,input().split()))
print(*(sorted(list(a_n^b_m))),sep=" ")

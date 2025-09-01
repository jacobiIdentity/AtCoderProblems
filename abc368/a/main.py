#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
print(*(a_n[n-k:]+a_n[:n-k]))

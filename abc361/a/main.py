#!/usr/bin/env python3
n,k,x = map(int ,input().split())
a_n = list(map(int ,input().split()))
print(*(a_n[:k]+[x]+a_n[k:]))

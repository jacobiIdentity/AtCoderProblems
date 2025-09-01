#!/usr/bin/env python3
n,q = map(int,input().split())
a_n = list(map(int,input().split()))
pos = {i:i for i in range(n)}
for i in range(q)
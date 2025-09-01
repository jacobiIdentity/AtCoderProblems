#!/usr/bin/env python3
n,m = map(int,input().split())
imos = [0]*(n+1)
for _ in range(m) :
    l,r = map(int,input().split())
    imos[l-1] += 1
    imos[r] -= 1
for i in range(n) :
    imos[i+1] += imos[i]
imos.pop()
print(min(imos))
#!/usr/bin/env python3
n,m = map(int,input().split())
s = input()
t = input()
imos = [0]*(n+1)
for _ in range(m) :
    a,b = map(int,input().split())
    imos[a-1] += 1
    imos[b] -= 1
for i in range(1,n+1) :
    imos[i] += imos[i-1]
# print(imos)
print("".join([t[i] if imos[i]%2 else s[i] for i in range(n)]))
#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(set(map(int,input().split())))
a_n.sort()
m = -1
for i in range(min(k,len(a_n))) :
    if a_n[i] != i :
        m = i
        break
if m == -1 : m = min(k,len(a_n))
print(m)
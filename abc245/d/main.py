#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
a_n.reverse()
c_nm = list(map(int,input().split()))
c_nm.reverse()
b_mn = [0]*(m+1)
for i in range(m+1) :
    b_mn[i] = c_nm[i]//a_n[0]
    for j in range(n+1) :
        c_nm[i+j] -= a_n[j]*b_mn[i]
print(*reversed(b_mn))
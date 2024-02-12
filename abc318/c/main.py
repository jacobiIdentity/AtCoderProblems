#!/usr/bin/env python3
n, d, p = map(int, input().split())
f_n = sorted(list(map(int, input().split())), reverse=True)
t = n//d+1
for i in range(n//d+1) :
    if i == n//d :
        if sum(f_n[i*d:n]) < p :
            t = i
            break
    if sum(f_n[i*d:i*d+d]) < p :
        t = i
        break
# print(t,n//d)
print( p*t + (0 if t == n//d+1 else sum(f_n[d*t:])))
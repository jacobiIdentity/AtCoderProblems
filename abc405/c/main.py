#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
ans = sum(a_n)**2
for i in range(n) :
    ans -= a_n[i]**2
print(ans//2)
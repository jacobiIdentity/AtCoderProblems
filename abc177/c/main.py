#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
ans = sum(a_n)
ans *= ans
for a_i in a_n :
    ans -= a_i*a_i
print((ans//2)%(10**9+7))
#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
f = [0]*(n+2)
f[1] = 1
mod = 10**9+7
for i in range(2,n+2) :
    f[i] = f[i-1]+f[i-2]
    f[i] %= mod
# print(f)
ans = 0
for i in range(n) :
    tmp = (f[n+1-i]*f[i+1])%mod
    tmp -= (f[n-i]*f[i])%mod
    tmp *= a_n[i]
    tmp %= mod
    ans += tmp
print(ans%mod)
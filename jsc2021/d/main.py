#!/usr/bin/env python3
n,p = map(int,input().split())
mod = 10**9+7
ans = p-1
ans *= pow(p-2,n-1,mod)
ans %= mod
print(ans)
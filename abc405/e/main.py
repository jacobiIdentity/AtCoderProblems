#!/usr/bin/env python3
import math
P = 998244353
def cmb(n, r, p=P):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
a,b,c,d = map(int,input().split())
n = max(a+b+c,d+c-1)

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % P)
    inv.append((-inv[P % i] * (P // i)) % P)
    factinv.append((factinv[-1] * inv[-1]) % P)


# former = cmb(a+b+c,b)
# latter = 1
# ans = former * latter
# ans %= P
ans = 0
for i in range(c+1) :
    
    ans += cmb(a+b+c-i,b) * cmb(d-1+i,d-1)
    ans %=P
print(ans)
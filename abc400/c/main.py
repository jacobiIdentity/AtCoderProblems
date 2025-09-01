#!/usr/bin/env python3
import math
n = int(input())
ans2 = 0
for i in range(1,3) :
    pow2a=2**i    
    if pow2a > n :
        break
    ok,ng = 1,10**9
    while ng -ok > 1 :
        mid = (ok+ng)//2
        if pow2a*mid*mid <= n :
            ok = mid
        else :
            ng = mid
    ans2 += ok

print(ans2)
#!/usr/bin/env python3
n = int(input())
ans = 1
pow2 = 2
for _ in range(n) :
    s = input()
    if s == 'OR' :
        ans = 2*ans+(pow2-ans)
    pow2 *= 2
print(ans)
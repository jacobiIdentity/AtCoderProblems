#!/usr/bin/env python3
import math
n = int(input())
ans = 1
for _ in range(n) :
    t_i = int(input())
    gcd = math.gcd(ans, t_i)
    ans = (ans//gcd) * (t_i//gcd) * gcd
print(ans)

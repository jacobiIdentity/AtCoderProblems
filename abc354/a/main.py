#!/usr/bin/env python3
h = int(input())
ans, now= 0, 0
while now <= h :
    now += 2**ans
    ans += 1
print(ans)
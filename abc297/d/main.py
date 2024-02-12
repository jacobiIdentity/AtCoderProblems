#!/usr/bin/env python3
a, b = map(int, input().split())
if a > b :
    a, b = b, a
ans = 0
while a!= 0 :
    ans += b//a
    a, b = b%a, a
if a == 1 :
    ans += 1
else :
    ans += a-1
print(ans)
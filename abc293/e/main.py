#!/usr/bin/env python3
a, x, m = map(int, input().split())
b, cnt, d = 1, 0, 1
while (cnt+1) * (cnt+1) < x:
    tmp = b
    b *= a
    b += 1
    d = b -tmp
    d %= m
    b %= m
    cnt += 1
d *= a
# print(b,d)
c, cnt = b, 0
while (cnt+1) * (cnt+1) < x:
    c *= d
    c += b
    c %= m
    cnt += 1
# print(c)
for _ in range(x-(cnt+1)*(cnt+1)) :
    c *= a
    c += 1
    c %= m
print(c%m)
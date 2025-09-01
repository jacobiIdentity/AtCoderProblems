#!/usr/bin/env python3
n,r = map(int,input().split())
ans = r
for _ in range(n) :
    d,a = map(int,input().split())
    if d == 1 and 1599 < ans < 2800 :
        ans += a
    elif d == 2  and 1199 < ans < 2400 :
        ans += a
print(ans)


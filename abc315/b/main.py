#!/usr/bin/env python3
m = int(input())
d_m = list(map(int, input().split()))
c = sum(d_m,1)//2
mm, dd, now = 1, 1, 0
while c > d_m[now]:
    c -= d_m[now]
    now += 1
    mm += 1
print(mm, c if c != 0 else d_m[now])
#!/usr/bin/env python3
n = int(input())
ps = [input().split() for _ in range(n)]
# print(ps)
my, mi = 10**11, 0
for i in range(n) :
    ny = int(ps[i][1])
    if ny < my :
        my, mi = ny, i
    # print(ny, i, my, mi)
# print(my, mi)
for i in range(n) :
    print(ps[(mi+i)%n][0])

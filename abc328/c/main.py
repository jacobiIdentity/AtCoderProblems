#!/usr/bin/env python3
n, q = map(int,input().split())
s = input()
sums = [0]*n
for i in range(1,n) :
    if s[i] == s[i-1] :
        sums[i] = sums[i-1]+1
    else :
        sums[i] = sums[i-1]
# print(sums)
for _ in range(q) :
    l, r = map(int,input().split())
    print(sums[r-1]-sums[l-1])

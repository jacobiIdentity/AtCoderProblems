#!/usr/bin/env python3
n,d,h = map(int,input().split())
ans = 0
for _ in range(n) :
    d1,h1 = map(int,input().split())
    ans = max(h-(d*(h-h1)/(d-d1)),ans)
print(ans)
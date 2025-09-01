#!/usr/bin/env python3
n,l,r = map(int,input().split())
ans = 0
for _ in range(n) :
    x,y = map(int,input().split())
    ans += 1 if (x<=l) and (r<=y) else 0
print(ans)
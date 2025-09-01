#!/usr/bin/env python3
n,m = map(int,input().split())
ng = set()
for _ in range(m) :
    a,b = map(int,input().split())
    ng.add((a,b))
    if (1<=a+2<=n and 1<=b+1<=n) :
        ng.add((a+2,b+1))
    if (1<=a+1<=n and 1<=b+2<=n) :
        ng.add((a+1,b+2))
    if (1<=a-1<=n and 1<=b+2<=n) :
        ng.add((a-1,b+2))
    if (1<=a-2<=n and 1<=b+1<=n) :
        ng.add((a-2,b+1))
    if (1<=a-2<=n and 1<=b-1<=n) :
        ng.add((a-2,b-1))
    if (1<=a-1<=n and 1<=b-2<=n) :
        ng.add((a-1,b-2))
    if (1<=a+1<=n and 1<=b-2<=n) :
        ng.add((a+1,b-2))
    if (1<=a+2<=n and 1<=b-1<=n) :
        ng.add((a+2,b-1))
print(n*n-len(ng))
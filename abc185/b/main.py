#!/usr/bin/env python3
n,m,t = map(int,input().split())
now = n
tnow = 0
isN = False
for _ in range(m) :
    a,b = map(int,input().split())
    now -= (a-tnow)
    if now <= 0 : 
        isN = True
        break
    now += (b-a)
    now = min(now,n)
    # print(a,b,now)
    tnow = b
if now-(t-b) <= 0 : isN = True
print("YNeos"[isN::2])
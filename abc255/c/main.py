#!/usr/bin/env python3
x,a,d,n = map(int,input().split())
aLast = a+(n-1)*d
if d == 0 :
    print(abs(x-a))
    exit()
if d < 0 :
    d *= -1
    a,aLast = aLast,a
if x <= a :
    print(a-x)
    exit()
if x >= aLast :
    print(x-aLast)
    exit()
k = (x-a)//d
print(min(x-a-k*d,a+(k+1)*d-x))
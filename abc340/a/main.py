#!/usr/bin/env python3
a,b,d = map(int,input().split())
now = a
while True :
    if now == b :
        print(now)
        break
    else :
        print(now, end=" ")
        now += d
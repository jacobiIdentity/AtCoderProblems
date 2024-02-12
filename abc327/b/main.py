#!/usr/bin/env python3
b = int(input())
a = 1
while a**a < 10**18+1 :
    if b == a**a :
        print(a)
        exit()
    a+=1
print(-1)
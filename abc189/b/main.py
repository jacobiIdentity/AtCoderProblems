#!/usr/bin/env python3
n,x = map(int,input().split())
x *= 100
drunk = 0
for i in range(n) :
    v,p = map(int,input().split())
    drunk += v*p
    if drunk > x :
        print(i+1)
        exit()    
print(-1)
#!/usr/bin/env python3
a,b = map(int,input().split())
x,y = a,b
while x>0 :
    x,y = y%x,x
print((a*b)//y)
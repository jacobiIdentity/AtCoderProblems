#!/usr/bin/env python3
x,y,n = map(int,input().split())
print(x*n if x*3 < y else (y*(n//3)+x*(n%3)) )

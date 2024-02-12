#!/usr/bin/env python3
n = int(input())
if abs(5*(n//5)-n) < abs(5*(n//5+1)-n) :
    print(5*(n//5))
else :
    print(5*(n//5+1))

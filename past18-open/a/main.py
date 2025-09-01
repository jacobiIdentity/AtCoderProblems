#!/usr/bin/env python3
x,y,z,s = map(int,input().split())
print('YNeos'[not(max(x,y,z)>=s)::2])
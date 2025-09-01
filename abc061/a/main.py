#!/usr/bin/env python3
a,b,c = map(int,input().split())
print('YNeos'[not(a<=c<=b)::2])
#!/usr/bin/env python3
import math 
a,b,c = map(int,input().split())
print((a|b)-(a&b)-(a^b))
print(math.comb(60,30))
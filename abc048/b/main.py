#!/usr/bin/env python3
import itertools
a,b,x = map(int,input().split())
print(b//x - (-1 if a==0 else (a-1)//x))
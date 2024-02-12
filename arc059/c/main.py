#!/usr/bin/env python3
from functools import reduce
from operator import add
n = int(input())
a_n = list(map(int, input().split()))
ave = sum(a_n)//n
print(min(reduce(add, map(lambda x: (x-ave)**2, a_n))\
        , reduce(add, map(lambda x: (x-ave-1)**2, a_n))))
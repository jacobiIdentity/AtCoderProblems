#!/usr/bin/env python3
import itertools
h,w,x = map(int,input().split())
p,q = map(int,input().split())
p -= 1
q -= 1
grid = [input() for _ in range(h)]

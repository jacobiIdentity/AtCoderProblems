#!/usr/bin/env python3
import sys
n = int(input())
x_n = sorted(list(map(int, input().split())))[n:4*n]
print(sum(x_n)/(3*n))
#!/usr/bin/env python3
n = int(input())
print(sum([((-1)**i) * (i**3) for i in range(n+1)] ))
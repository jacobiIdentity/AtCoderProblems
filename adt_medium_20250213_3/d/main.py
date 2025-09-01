#!/usr/bin/env python3
x = int(input())
print(sum(sum([[(i*j if i*j!=x else 0) for i in range(1,10)]for j in range(1,10)],[])))

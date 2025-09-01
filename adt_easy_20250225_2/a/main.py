#!/usr/bin/env python3
n = int(input())
print('Yes' if 2*([input() for _ in range(n)].count('For'))>n else 'No')
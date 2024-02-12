#!/usr/bin/env python3
n,x = map(int, input().split())
print('Yes' if x >= (sum(map(int, input().split())) -n//2) else 'No')

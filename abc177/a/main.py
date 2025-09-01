#!/usr/bin/env python3
d,t,s = map(int, input().split())
print('Yes' if t*s-d >=0 else 'No')
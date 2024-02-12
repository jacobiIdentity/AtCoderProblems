#!/usr/bin/env python3
x, y = map(int, input().split())
print('Yes' if (y-x < 3 and y-x > -4) else 'No')

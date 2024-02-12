#!/usr/bin/env python3
a, b = map(int, input().split())
print('Yes' if (b-a == 1 and a%3 != 0) else 'No')

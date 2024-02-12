#!/usr/bin/env python3
n, k, a = map(int, input().split())
print((a+k-1)%n if (a+k-1)%n != 0 else n)
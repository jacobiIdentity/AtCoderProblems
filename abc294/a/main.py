#!/usr/bin/env python3
n = int(input())
print(*list(filter(lambda x: x%2 == 0, map(int, input().split()))))

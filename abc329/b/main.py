#!/usr/bin/env python3
n = int(input())
a_n = set(map(int, input().split()))
t = max(a_n)
a_n.discard(t)
print(max(a_n))
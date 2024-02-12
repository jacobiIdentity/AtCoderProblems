#!/usr/bin/env python3
n = int(input())
p_n = list(map(int, input().split()))
a, b = max(p_n), p_n[0]
print((a-b+1) if a != b else 1 if p_n.count(a) > 1 else 0)

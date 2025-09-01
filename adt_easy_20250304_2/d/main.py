#!/usr/bin/env python3
n,k = map(int,input().split())
s_n = [input() for _ in range(n)][:k]
s_n.sort()
print('\n'.join(s_n))

#!/usr/bin/env python3
n = int(input())
s_n = [input() for _ in range(n)]
s_n.sort(key=lambda x:len(x))
print(''.join(s_n))

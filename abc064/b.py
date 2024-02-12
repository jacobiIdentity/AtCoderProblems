#!/usr/bin/env python3
n = int(input())
a_n = list(set(map(int, input().split())))
print(max(a_n)-min(a_n))

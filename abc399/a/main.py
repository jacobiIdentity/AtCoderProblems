#!/usr/bin/env python3
n = int(input())
s = input()
t = input()
ans = [1 if s[i]!=t[i] else 0 for i in range(n)]
print(sum(ans))
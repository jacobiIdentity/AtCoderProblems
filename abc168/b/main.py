#!/usr/bin/env python3
k = int(input())
s = input()
print(s if len(s)<k+1 else s[:k]+"...")
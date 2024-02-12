#!/usr/bin/env python3
n, k = map(int, input().split())
notAns = set()
for _ in range(k) :
    d = input()
    notAns |= set(map(int, input().split()))
print(n-len(notAns))

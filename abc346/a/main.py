#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
print(*list(map(lambda i:a_n[i]*a_n[i+1], range(n-1))))

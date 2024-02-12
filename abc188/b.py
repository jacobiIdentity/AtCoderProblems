#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))
ip = 0
for i in range(n) : ip += a_n[i]*b_n[i]
print('No' if ip else 'Yes')

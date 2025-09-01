#!/usr/bin/env python3
n = int(input())
x_n = list(map(int,input().split()))
print(sum(abs(x) for x in x_n))
print(pow(sum(x*x for x in x_n),0.5))
print(max(abs(x) for x in x_n))

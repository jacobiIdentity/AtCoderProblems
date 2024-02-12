#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
print((n+1)*(n+2*min(a_n))//2-sum(a_n))
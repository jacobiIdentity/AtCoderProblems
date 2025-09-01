#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
s_t = [list(map(int, input().split())) for _ in range(n-1)]
for i in range(n-1) :
    a_n[i+1] += (a_n[i]//s_t[i][0])*s_t[i][1]
print(a_n[n-1])
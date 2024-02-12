#!/usr/bin/env python3
n, q = map(int, input().split())
a_ij = [list(map(int, input().split())) for _ in range(n)]
for _ in range(q) :
    s, t = map(int, input().split())
    print(a_ij[s-1][t])

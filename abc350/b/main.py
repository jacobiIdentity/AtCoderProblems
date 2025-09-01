#!/usr/bin/env python3
n, q = map(int, input().split())
t_q = list(map(int, input().split()))
teeth = [1]*n
for i in range(q) :
    teeth[t_q[i]-1] = 1-teeth[t_q[i]-1]
print(sum(teeth))
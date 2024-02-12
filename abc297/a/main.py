#!/usr/bin/env python3
n, d = map(int, input().split())
t_n = list(map(int, input().split()))
ans = -1
for i in range(1, n) :
    if t_n[i] - t_n[i-1] <= d :
        ans = t_n[i]
        break
print(ans)

#!/usr/bin/env python3
n = int(input())
a_n = sorted(map(int, input().split()))
ans = 1
for i in range(n) :
    ans *= max(a_n[i] - i,0)
    ans %= 10**9+7
print(ans)
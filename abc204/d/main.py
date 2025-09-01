#!/usr/bin/env python3
n = int(input())
t_n = list(map(int, input().split()))

S = sum(t_n)
dp = [False] * (S + 1)
dp[0] = True

for t in t_n:
    for i in range(S, t - 1, -1):
        if dp[i - t]:
            dp[i] = True

# S // 2 に最も近い True の値を探す
for i in range(S // 2, -1, -1):
    if dp[i]:
        print(max(S-i,i))
        break

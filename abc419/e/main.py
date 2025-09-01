#!/usr/bin/env python3
# import itertools
# acs = list(itertools.accumulate([0]+a_n))
# # print(a_n)
# # print(acs)
# costs = [[[0]*m for _ in range(m)] for _ in range(l)]
# for i in range(l):
#     for j in range(m) :
#         for k in range(m) :
#             o
# dp = [[float('inf')]*m for _ in range(l+1)]
# for i in range(l) :
#     for 


n, l, m = map(int, input().split())
a_n = list(map(int, input().split()))

# W[j][u][v]:
# P'[j] ≡ u, P'[j+1] ≡ v としたときの「k≡j(mod L)の全要素」のコスト
W = [[[0]*m for _ in range(m)] for _ in range(l)]

for i in range(l):
    # j番目のクラスの要素たち (k=j, j+L, j+2L, ...)
    indices = range(i, n, l)
    for u in range(m):
        for v in range(m):
            total_cost = 0
            diff = (v - u) % m  # このクラスの A'[k] の余り
            for k in indices:
                need = diff
                have = a_n[k] % m
                # have を need に揃えるために何回 +1 するか
                cost = (need - have) % m
                total_cost += cost
            W[i][u][v] = total_cost

# DP配列
dp = [[float("inf")]*m for _ in range(l+1)]
dp[0][0] = 0  # P'[0] = 0 が固定

for i in range(l+1):
    for u in range(m):
        if dp[i][u] == float("inf"):
            continue
        for v in range(m):
            dp[i+1][v] = min(dp[i+1][v], dp[i][u] + W[i][u][v])

ans = dp[l][0]  # P'[L] ≡ 0 にする
print(ans)
print(dp)
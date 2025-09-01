#!/usr/bin/env python3
from collections import defaultdict

n, k = map(int, input().split())
p_n = list(map(int, input().split()))

# 巡回置換を探す
cyc = defaultdict(list)
visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    v = i
    while not visited[v]:
        visited[v] = True
        cyc[i].append(v)
        v = p_n[v] - 1  # 0-indexに合わせる

# 結果の置換
final_p = [-1] * n

# 各巡回に対してk回適用した結果を求める
for key in cyc:
    cycle = cyc[key]
    cycle_len = len(cycle)
    # kを巡回の長さで縮小
    effective_k = pow(2,k,cycle_len)
    # print(cycle_len,effective_k,cycle)
    for i, idx in enumerate(cycle):
        # effective_k回適用後の位置を計算する
        new_idx = (i + effective_k) % cycle_len
        # cycle[new_idx]に対応する場所を、元の位置で更新
        final_p[idx] = cycle[new_idx]+1

# 1始まりに戻して表示（全要素を+1して表示する）
print(' '.join(map(str, final_p)))

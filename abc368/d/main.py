#!/usr/bin/env python3
import sys
# import pypyjit
from collections import defaultdict

sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

def dfs(v):
    visited[v-1] = True
    hasV_kChildNode = v in v_k_set
    for neighbor in tree[v]:
        if not visited[neighbor-1]:
            if dfs(neighbor):
                hasV_kChildNode = True
    if not hasV_kChildNode:
        removed.add(v)
    return hasV_kChildNode

# 入力の読み込み
n, k = map(int, input().split())
tree = defaultdict(set)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)
v_k = list(map(int, input().split()))

# 初期化
visited = [False] * n
removed = set()
v_k_set = set(v_k)

# DFS開始
dfs(v_k[0])

# 残ったノード数の出力
print(n - len(removed))
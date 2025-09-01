#!/usr/bin/env python3
from collections import deque
n = int(input())
a_ij = [list(map(int,input().split())) for _ in range(2*n-1)]
# ans = 0
# all_idx = range(2*n)
# for cmb in itertools.combinations(all_idx,n) :
#     fsts = list(cmb)
#     scnds = list(set(all_idx)-set(fsts))
#     for nums1 in itertools.permutations(range(n)) :
#         for nums2 in itertools.permutations(range(n)) :
#             tmp = 0
#             for i in range(n) :
#                 x,y = fsts[nums1[i]],scnds[nums2[i]]
#                 if x>y :
#                     x,y = y,x
#                 tmp ^= a_ij[x][y-x-1]
#             ans = max(ans,tmp)
# print(ans)

size = 2*n
dp = [-1] * (1 << (2*n))
dp[0] = 0 

queue = deque([0])

while queue:
    mask = queue.popleft()
    val = dp[mask]

    # 選んでいない最初の要素
    for first in range(size):
        if not (mask & (1 << first)):
            break
    else:
        continue

    # first とペアになる j をすべて探索
    for j in range(size):
        if j == first or (mask & (1 << j)):
            continue
        x, y = first, j
        if x > y:
            x, y = y, x
        new_mask = mask | (1 << first) | (1 << j)
        new_val = val ^ a_ij[x][y-x-1]
        if dp[new_mask] < new_val:
            dp[new_mask] = new_val
            queue.append(new_mask)  # 更新があれば再探索

# stack = [0]  # 初期状態は mask=0
# while stack:
#     mask = stack.pop()
#     val = dp[mask]
#     # 選んでいない最初の要素を固定
#     for first in range((2*n)):
#         if not (mask & (1 << first)):
#             break
#     else:
#         continue  # 全て選択済み

#     # first とペアになる j を選ぶ
#     for j in range((2*n)):
#         if mask & (1 << j) or j == first:
#             continue
#         x, y = first, j
#         if x > y:
#             x, y = y, x
#         new_mask = mask | (1 << first) | (1 << j)
#         new_val = val ^ a_ij[x][y-x-1]
#         if dp[new_mask] < new_val:
#             dp[new_mask] = new_val
#             stack.append(new_mask)

print(dp[-1])
# for mask in range(1 << (2*n)):
#     if dp[mask] is None:
#         continue
#     if (bin(mask).count("1")) % 2 :
#         continue
#     # ペアにする2つの要素を選ぶ
#     for i in range(size):
#         if mask & (1 << i):
#             continue
#         for j in range(i+1, size):
#             if mask & (1 << j):
#                 continue
#             x, y = i, j
#             if x > y:
#                 x, y = y, x
#             new_mask = mask | (1 << i) | (1 << j)
#             val = dp[mask] ^ a_ij[x][y-x-1]
#             if dp[new_mask] is None or dp[new_mask] < val:
#                 dp[new_mask] = val

# print(dp[(1 << size)-1])

# import sys
# sys.setrecursionlimit(1 << 25)
# from functools import lru_cache

# n = int(input())
# a_ij = [list(map(int,input().split())) for _ in range(2*n-1)]
# size = 2*n

# @lru_cache(maxsize=None)
# def dfs(mask):
#     if mask == (1 << size) - 1:
#         return 0

#     for first in range(size):
#         if not (mask & (1 << first)):
#             break

#     res = 0
#     for j in range(first+1, size):
#         if not (mask & (1 << j)):
#             x, y = first, j
#             if x > y:
#                 x, y = y, x
#             new_mask = mask | (1 << first) | (1 << j)
#             res = max(res, dfs(new_mask) ^ a_ij[x][y-x-1])
#     return res

# print(dfs(0))
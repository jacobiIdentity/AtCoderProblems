#!/usr/bin/env python3
# h,w,q = map(int,input().split())
# grid = [[1]*w for _ in range(h)]
# ans = h*w
# for _ in range(q) :
#     r,c = map(int,input().split())
#     if grid[r-1][c-1] == 1 :
#         ans -= 1
#         grid[r-1][c-1] = 0
#     else :
#         tmp = r-2
#         # up
#         while tmp > -1 :
#             if grid[tmp][c-1] == 1 :
#                 grid[tmp][c-1] = 0
#                 ans -= 1
#                 break
#             tmp -= 1
#         # down
#         tmp = r
#         while tmp < h :
#             if grid[tmp][c-1] == 1 :
#                 grid[tmp][c-1] = 0
#                 ans -= 1
#                 break
#             tmp += 1
#         tmp = c-2
#         # left
#         while tmp > -1 :
#             if grid[r-1][tmp] == 1 :
#                 grid[r-1][tmp] = 0
#                 ans -= 1
#                 break
#             tmp -= 1
#         # down
#         tmp = c
#         while tmp < w :
#             if grid[r-1][tmp] == 1 :
#                 grid[r-1][tmp] = 0
#                 ans -= 1
#                 break
#             tmp += 1
# print(ans)

from collections import deque

def process_queries(h, w, queries):
    deleted = set()
    remaining_cells = h * w
    
    # 四方向の移動
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, c in queries:
        r -= 1
        c -= 1
        
        if (r, c) in deleted:
            # 削除済みセルの場合、最も近いセルを削除する
            for dr, dc in directions:
                nr, nc = r, c
                while 0 <= nr < h and 0 <= nc < w:
                    nr += dr
                    nc += dc
                    if 0 <= nr < h and 0 <= nc < w:
                        if (nr, nc) not in deleted:
                            deleted.add((nr, nc))
                            remaining_cells -= 1
                            break
                    else:
                        break
                if remaining_cells < 1:
                    break
        else:
            # 削除されていないセルを削除
            deleted.add((r, c))
            remaining_cells -= 1

    return remaining_cells

# 入力の処理
h, w, q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# 処理と出力
result = process_queries(h, w, queries)
print(result)

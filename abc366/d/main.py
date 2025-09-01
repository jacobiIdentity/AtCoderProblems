#!/usr/bin/env python3
import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0

    # nの読み込み
    n = int(data[idx])
    idx += 1

    # 配列Aの読み込み
    A = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                A[i][j][k] = int(data[idx])
                idx += 1

    # 累積和の配列
    cumsum = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                cumsum[i][j][k] = (A[i][j][k]
                                   + cumsum[i-1][j][k]
                                   + cumsum[i][j-1][k]
                                   + cumsum[i][j][k-1]
                                   - cumsum[i-1][j-1][k]
                                   - cumsum[i-1][j][k-1]
                                   - cumsum[i][j-1][k-1]
                                   + cumsum[i-1][j-1][k-1])

    # クエリの数を読み込む
    q = int(data[idx])
    idx += 1

    results = []
    for _ in range(q):
        Lx = int(data[idx])
        Rx = int(data[idx+1])
        Ly = int(data[idx+2])
        Ry = int(data[idx+3])
        Lz = int(data[idx+4])
        Rz = int(data[idx+5])
        idx += 6

        result = (cumsum[Rx][Ry][Rz]
                  - (cumsum[Lx-1][Ry][Rz] if Lx > 1 else 0)
                  - (cumsum[Rx][Ly-1][Rz] if Ly > 1 else 0)
                  - (cumsum[Rx][Ry][Lz-1] if Lz > 1 else 0)
                  + (cumsum[Lx-1][Ly-1][Rz] if Lx > 1 and Ly > 1 else 0)
                  + (cumsum[Lx-1][Ry][Lz-1] if Lx > 1 and Lz > 1 else 0)
                  + (cumsum[Rx][Ly-1][Lz-1] if Ly > 1 and Lz > 1 else 0)
                  - (cumsum[Lx-1][Ly-1][Lz-1] if Lx > 1 and Ly > 1 and Lz > 1 else 0))

        results.append(str(result))

    sys.stdout.write("\n".join(results) + "\n")

# メイン実行部分
if __name__ == "__main__":
    solve()

# n = int(input())
# a = [[list(map(int,input().split())) for _ in range(n)]for _ in range(n)]

# import numpy as np

# # n の設定
# n = int(input())

# # 標準入力から A を受け取る
# A = np.zeros((n+1, n+1, n+1), dtype=int)

# # 標準入力からデータを読み取って A に格納
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         row = list(map(int, input().split()))
#         for k in range(1, n+1):
#             A[i][j][k] = row[k-1]

# # 累積和の配列を準備
# cumsum = np.cumsum(np.cumsum(np.cumsum(A, axis=0), axis=1), axis=2)

# # クエリ数 q の設定
# q = int(input())

# # 各クエリに対して範囲の和を求める
# for _ in range(q):
#     Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())

#     # Lx-1, Ly-1, Lz-1 からの累積和を引いて調整する
#     result = (cumsum[Rx, Ry, Rz]
#              - (cumsum[Lx-1, Ry, Rz] if Lx > 1 else 0)
#              - (cumsum[Rx, Ly-1, Rz] if Ly > 1 else 0)
#              - (cumsum[Rx, Ry, Lz-1] if Lz > 1 else 0)
#              + (cumsum[Lx-1, Ly-1, Rz] if Lx > 1 and Ly > 1 else 0)
#              + (cumsum[Lx-1, Ry, Lz-1] if Lx > 1 and Lz > 1 else 0)
#              + (cumsum[Rx, Ly-1, Lz-1] if Ly > 1 and Lz > 1 else 0)
#              - (cumsum[Lx-1, Ly-1, Lz-1] if Lx > 1 and Ly > 1 and Lz > 1 else 0))

#     print(result)


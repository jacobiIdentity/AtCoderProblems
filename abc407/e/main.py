#!/usr/bin/env python3
import heapq
def max_constrained_sum(a):
    n = len(a) // 2

    # 左から順にn個の中で最大のi個を選ぶ
    left_heap = []
    left_sum = 0
    left_sums = [0] * (n + 1)

    for i in range(n):
        heapq.heappush(left_heap, a[i])
        left_sum += a[i]
    left_sums[0] = left_sum

    for i in range(n):
        heapq.heappush(left_heap, a[n + i])
        left_sum += a[n + i] - heapq.heappop(left_heap)
        left_sums[i + 1] = left_sum

    # 右から順にn個の中で最大のi個を選ぶ（逆から見る）
    right_heap = []
    right_sum = 0
    right_sums = [0] * (n + 1)

    for i in range(n):
        heapq.heappush(right_heap, -a[2 * n - 1 - i])
        right_sum += a[2 * n - 1 - i]
    right_sums[n] = right_sum

    for i in range(n - 1, -1, -1):
        heapq.heappush(right_heap, -a[i])
        right_sum += a[i] + heapq.heappop(right_heap)
        right_sums[i] = right_sum

    # 条件を満たす最大値を探索
    max_total = float('-inf')
    for i in range(n + 1):
        max_total = max(max_total, left_sums[i] - right_sums[i])
    return max_total
t = int(input())
for _ in range(t) :
    n  = int(input())
    a_n = [int(input()) for _ in range(2*n)]
    print(max_constrained_sum(a_n))
    
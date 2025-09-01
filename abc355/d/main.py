#!/usr/bin/env python3
def count_overlapping_intervals(intervals):
    events = []
    for l, r in intervals:
        events.append((l, 'L'))
        events.append((r, 'R'))
    
    # イベントを左端と右端でソート、同じ場合はLを先に処理する
    events.sort(key=lambda x: (x[0], x[1]))

    current_intervals = 0
    total_overlaps = 0

    for event in events:
        if event[1] == 'L':
            # 現在の重なり区間数をカウントに加える
            total_overlaps += current_intervals
            current_intervals += 1
        else:
            current_intervals -= 1

    return total_overlaps

# 標準入力から読み込む場合
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
intervals = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(N)]

# 結果を出力
print(count_overlapping_intervals(intervals))
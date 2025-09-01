#!/usr/bin/env python3
n, m = map(int, input().split())
a_b = [tuple(map(int,input().split())) for _ in range(n)]
c_d = [tuple(map(int,input().split())) for _ in range(m)]

ok, ng = 0.0, 1e5  # 強さは最大でも 100000
for _ in range(80):  # 収束させる
    mid = (ok + ng) / 2
    isOK = True
    scores = [b - mid*a for a, b in a_b]
    scores.sort(reverse=True)
    bestMonster = sum(scores[:5])

    bestWithHelper = float("-inf")
    bestWithHelper = max(d - mid*c for c, d in c_d) + sum(scores[:4])

    if max(bestMonster, bestWithHelper) >= 0 :
        ok = mid
    else:
        ng = mid

print(f"{ok:.15f}")

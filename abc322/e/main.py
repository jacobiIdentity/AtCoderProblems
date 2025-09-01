#!/usr/bin/env python3
from collections import deque
n, k, p = map(int, input().split())
c_a_nk = list(map(int, input().split()))
dp = [[10**12]*(k+1) for _ in range(n+1)]
dp2 = [[[0]*(n+1) for _ in range(k+1)] for _ in range(n+1)]
for i in range(0,n+1) :
    for j in range(0,k) :
        dp[i][j+1]


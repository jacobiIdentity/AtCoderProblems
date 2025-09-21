#!/usr/bin/env python3
from collections import defaultdict

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    s_h = [input().strip() for _ in range(h)]

    allBlacks = []
    for i in range(h-1):
        for j in range(w-1):
            if s_h[i][j] == s_h[i][j+1] == s_h[i+1][j] == s_h[i+1][j+1] == "#":
                allBlacks.append((i, j))

    if len(allBlacks) == 0 :
        print(0)
        continue

    m = len(allBlacks) 
    allbits = (1 << m) - 1

    changeWhiteBits = defaultdict(int)
    for k, (i, j) in enumerate(allBlacks):
        for x, y in [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]:
            changeWhiteBits[(x, y)] |= (1 << k)

    changeWhiteBitsVal = list(changeWhiteBits.values())
    dp = {}
    stack = [(0, 0)] 

    while stack:
        bits, state = stack.pop()
        if state == 0:
            if bits == allbits:
                dp[bits] = 0
                continue
            if bits in dp:
                continue
            stack.append((bits, 1))
            k = (allbits ^ bits).bit_length() - 1
            for cm in changeWhiteBitsVal:
                if cm & (1 << k):
                    nxt = bits | cm
                    if nxt not in dp:
                        stack.append((nxt, 0))
        else:
            k = (allbits ^ bits).bit_length() - 1
            now = m
            for cm in changeWhiteBitsVal:
                if cm & (1 << k):
                    nxt = bits | cm
                    now = min(now, 1 + dp[nxt])
            dp[bits] = now

    print(dp[0])
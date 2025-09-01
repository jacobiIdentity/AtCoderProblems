#!/usr/bin/env python3
h,w,k = map(int, input().split())
grid= [input() for _ in range(h)]
bAllCnt = sum([grid[i].count("#") for i in range(h)])
ans = 0
for bi in range(2<<(h+w-1)) :
    fmt = '#0{}b'.format(h+w+2)
    iBiStr = format(bi, fmt)[2:]
    tmp = 0
    for i in range(h) :
        for j in range(w) :
            tmp += 1 if iBiStr[i] != '1' and iBiStr[j+h] != '1' and grid[i][j] == '#' else 0
    ans += 1 if tmp == k else 0

print(ans)
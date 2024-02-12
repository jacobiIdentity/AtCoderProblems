#!/usr/bin/env python3
import sys
n, d = map(int, input().split())
s_n = [input() for _ in range(n)]
ans, tmp, flg = 0, 0, True
for i in range(d) :
    for j in range(n) :
        if s_n[j][i] == 'x' :
            ans = max(tmp, ans)
            tmp = 0
            flg = False
            break
        else :
            flg = True
    if flg :
        tmp += 1
print(max(ans, tmp))
